from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
import random
from django.conf import settings
from .models import Lib_user, Book, IssuedItem
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q



# Create your views here.

def st_index(request):
    books = Book.objects.all()
    users = IssuedItem.objects.all()
    if request.method == "GET":
        st = request.GET.get("search_value")
        if st != None:
            books = Book.objects.filter(book_name__icontains = st)
            
    try:
        user_obj = Lib_user.objects.get(email = request.session["email"])
        return render(request, "st_index.html", {"user_obj":user_obj, "books":books, "users":users})
    
    except:
        return render(request, "st_index.html")
def st_register(request):
     if request.method == "GET":
        return render(request, "st_register.html")

     elif request.method == "POST":
        if len(request.POST["pass"]) < 8:
            return render(request, "st_register.html",{"massage":"Password is too short!! at least 8 charcter requird:"})

        elif request.POST["pass"] == request.POST["re_pass"]:
            try:
                user_mail = Lib_user.objects.get(email = request.POST["email"])
                return render(request, "st_register.html",{"massage": "This email is already exist! please use another email:"})
            except:
                global user_dict
                user_dict = {
                    "uname": request.POST["uname"],
                    "mobile": request.POST["mobile"],
                    "email":request.POST["email"],
                    "password":request.POST["pass"],
                    "Repass" : request.POST["re_pass"]
                    }

                

                subject = "Registration!!!"
                global gen_otp
                gen_otp = random.randint(100000,999999)
                massage = f''' Hello {user_dict["uname"].upper()}.
                Your otp is {gen_otp}.'''
                from_email = settings.EMAIL_HOST_USER
                list1 = [request.POST["email"]]
                send_mail(subject,massage,from_email,list1)
                return render (request, "st_otp.html",{"massage":"Please check your mailbox"})

        else:
            return render(request, "st_register.html",{"massage":"Password and confirm password are not match!!Enter AGAIN:"})
    
def st_otp(request):
    if request.method == "POST":
        if gen_otp == int(request.POST["otp"]):
           Lib_user.objects.create(

           uname = user_dict["uname"],
           mobile = user_dict["mobile"],
           email =user_dict["email"],
           password = user_dict["password"],
    
           )
            
           return render(request, "st_register.html",{"massage":"Your Register successfull go and sing IN:"})

        else:
            return render(request, "st_otp.html",{"massage":"Your OTP is incorrect!! ENTER OTP AGAIN: "})

    else:
       return render(request, "st_register.html")


def st_signin(request):
    if request.method == "GET":
        return render(request, "st_signin.html")
    
    else:
        try:
            session_user = Lib_user.objects.get(email = request.POST["email"])
            if request.POST["pass"] == session_user.password:
                request.session["email"] = request.POST["email"]
                return redirect("st_index")

            else:
                return render(request, "st_signin.html",{"massage":"TRY AGAIN!!! Pasword is INCORRECT:"})


        except:
            return render(request,"st_signin.html",{"massage":"This Email is not EXIST !! Please register First or Enter correct Email:"})
        

def st_logout(request):
    del request.session["email"]
    return render(request, "st_index.html")



## create views to issue book to user
@login_required(login_url = "login")
def issue(request):

    #if the request is POST then get book id from request
    if request.method == "POST":
        book_id = request.POST["book_id"]
        # import pdb; pdb.set_trace()
        global user_id
        user_id =request.POST["user"]
        current_user = User.objects.get(id = user_id)
        user = User.objects.filter(id = user_id)
        current_book = Book.objects.get(id = book_id)
        book = Book.objects.filter(id = book_id)
        issue_item = IssuedItem.objects.create(
            user_id = current_user , book_id = current_book
        )
        issue_item.save()
        book.update(quantity=book[0].quantity - 1)

        # Show success message and redirect to issue page
        messages.success(request, "Book issued successfully.")

         # Get all books which are not issued to user
        my_items = IssuedItem.objects.filter(
            user_id=current_user , return_date__isnull=True
        ).values_list("book_id")
        books = Book.objects.exclude(id__in=my_items).filter(quantity__gt=0)

        # Return issue page with books that are not issued to user
        return render(request, "index.html", {"books" : books})
    else:
        return render(request, "issue_item.html")

# History view to show history of issued books to user
@login_required(login_url="login")
def history(request):


    # Get all issued books to user
    user_obj = User.objects.get(email = request.session["email"])
    my_items = IssuedItem.objects.filter(user_id=user_obj.id).order_by("-issue_date")

    # Paginate data
    paginator = Paginator(my_items, 10)

    # Get page number from request
    page_number = request.GET.get("page")
    show_data_final = paginator.get_page(page_number)

    # Return history page with issued books to user
    return render(request, "history.html", {"books": show_data_final})


# Return view to return book to library
@login_required(login_url="login")
def return_item(request):

    # If request is post then get book id from request
    if request.method == "POST":

        # Get book id from request
        book_id = request.POST["book_id"]

        # Get book object
        current_book = Book.objects.get(id=book_id)

        # Update book quantity
        book = Book.objects.filter(id=book_id)
        book.update(quantity=book[0].quantity + 1)

        # Update return date of book and show success message
        issue_item = IssuedItem.objects.filter(
            user_id=request.user, book_id=current_book, return_date__isnull=True
        )
        issue_item.update(return_date=date.today())
        messages.success(request, "Book returned successfully.")


    # Get all books which are issued to user
    my_items = IssuedItem.objects.filter(
        user_id=request.user, return_date__isnull=True
    ).values_list("book_id")
    # Get all books which are not issued to user
    books = Book.objects.exclude(~Q(id__in=my_items))
    # Return return page with books that are issued to user
    params = {"books": books}
    return render(request, "return_item.html", params)

## adding book 
def add_new(request):
    user_obj = Lib_user.objects.get(email = request.session["email"])
    books = Book.objects.all()
    users = IssuedItem.objects.all()
    if request.method == "GET":
        return render(request, "issue_item.html")
    else:
        Book.objects.create(
            book_name = request.POST["book_name"],
            author_name = request.POST["author_name"],
            quantity = request.POST["quantity"],
            book_add_time = request.POST["book_add_time"],
            book_add_date = request.POST["book_add_date"]
        )
        return render(request, "st_index.html",{"message":"Your book has been successfully added!!!", "user_obj":user_obj, "books":books, "users": users })


def all_books(request):
    return render(request, "history.html")

def req_book(request):
    all_item = IssuedItem.objects.all()
    return render(request, "request_book.html", {"all_item": all_item})