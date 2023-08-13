from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.index, name="index"),
    path("",views.register, name="register"),
    path("register/", views.register, name="register"),
    path("signup/", views.signup, name="signup"),
    path("otp/", views.otp, name="otp"),
    path("logout/", views.logout, name="logout"),
    path("request/", views.request, name='request'),
   
]