from django.urls import path
from . import views

urlpatterns = [
    path("",views.st_index, name="st_index"),
    path("st_login/",views.st_register, name="st_login"),
    path("st_otp/", views.st_otp, name="st_otp"),
    path("st_signup/", views.st_signin, name="st_signup"),
    path("st_logut/", views.st_logout, name="st_logout"),
    path("issue/",views.issue, name ="issue"),
    path("add_new/", views.add_new, name="add_new"),
    path("history/",views.history, name='history'),
    path("all_books/",views.all_books,name="all_books"),
    path("req_book/", views.req_book, name="req_book"),
    

]