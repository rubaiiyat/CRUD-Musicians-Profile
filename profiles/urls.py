from django.urls import path, include
from . import views

urlpatterns = [
    path("auth/register/", views.register, name="register"),
    path("auth/login/", views.userLogin, name="login"),
    path("", views.profiles, name="profile"),
]
