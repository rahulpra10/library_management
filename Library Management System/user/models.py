from django.db import models

# Create your models here.

### user table

class User(models.Model):
    uname = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    pic = models.FileField(upload_to="profile",default="avtar.webp",null=True)
    

    def __str__(self) -> str:
        return self.uname
    
class Request(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    year = models.CharField(max_length=10)
    deadline = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.title
    