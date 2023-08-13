from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import random
from .models import *
from lib_user.models import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

## home page
def index(request):
    books = Book.objects.all()
    try:
        # import pdb;pdb.set_trace()
        user_obj = User.objects.get(email = request.session["email"])
        return render(request, "index.html", {"user_obj":user_obj, "books":books})
    
    except:
        return render(request, "index.html")

#### Registration process
def register(request):
     if request.method == "GET":
        return render(request, "register.html")

     elif request.method == "POST":
        if len(request.POST["pass"]) < 8:
            return render(request, "register.html",{"massage":"Password is too short!! at least 8 charcter requird:"})

        elif request.POST["pass"] == request.POST["re_pass"]:
            try:
                user_mail = User.objects.get(email = request.POST["email"])
                return render(request, "register.html",{"massage": "This email is already exist! please use another email:"})
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
                return render (request, "otp.html",{"massage":"Please check your mailbox"})

        else:
            return render(request, "register.html",{"massage":"Password and confirm password are not match!!Enter AGAIN:"})
    
def otp(request):
    if request.method == "POST":
       if gen_otp == int(request.POST["otp"]):
           User.objects.create(

           uname = user_dict["uname"],
           mobile = user_dict["mobile"],
           email =user_dict["email"],
           password = user_dict["password"],
    
           )
            
           return render(request, "register.html",{"massage":"Your Register successfull go and sing IN:"})

       else:
           return render(request, "otp.html",{"massage":"Your OTP is incorrect!! ENTER OTP AGAIN: "})

    else:
       return render(request, "register.html")

def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")
    
    else:
        try:
            session_user = User.objects.get(email = request.POST["email"])
            if request.POST["pass"] == session_user.password:
                request.session["email"] = request.POST["email"]
                return redirect("index")

            else:
                return render(request, "signup.html",{"massage":"TRY AGAIN!!! Pasword is INCORRECT:"})


        except:
            return render(request,"signup.html",{"massage":"This Email is not EXIST !! Please register First or Enter correct Email:"})
        

def logout(request):
    del request.session["email"]
    return render(request, "index.html")

def request(request):
    if request.method == "POST":
        messages.success(request, "Your request has been sent succesfully!!!")
    
        new_dict = {
            "title" : request.POST["title"],
            "author" : request.POST["author"],
            "date" : request.POST["year"],
            "deadline" : request.POST["deadline"]
        }

        Request.objects.create(
            title = new_dict["title"],
            author = new_dict["author"],
            year = new_dict["date"],
            deadline = new_dict["deadline"]
        )
        return render(request, "index.html")

    else:
        return render(request, "request.html")
    



