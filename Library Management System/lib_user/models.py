from django.db import models
from user.models import User
from datetime import date
from django.utils import timezone

# Create your models here.
class Lib_user(models.Model):
    uname = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    pic = models.FileField(upload_to="st_profile",default="avtar.webp",null=True)
    

    def __str__(self) -> str:
        return self.uname


## Book model to store book details

class Book(models.Model):
    book_name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=30)
    quantity = models.IntegerField(default=1)
    book_add_time = models.TimeField(default= timezone.now())
    book_add_date = models.DateField(default=date.today())

    class Meta:
        unique_together = ("book_name","author_name")

    def __str__(self) -> str:
        return self.book_name


## Issueditem model to store issued book details

class IssuedItem(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_date = models.DateField(default=date.today(), blank=False)
    return_date = models.DateField(blank=True, null=True)

    #property to get book name
    def book_name(self):
        return self.book_id.book_name
    
    #property to get author name
    def username(self):
        return self.user_id.uname
    
    def __str__(self) -> str:
        return (self.book_id.book_name +
                " Issued by " + self.user_id.uname +
                " On " + str(self.issue_date)
                )



