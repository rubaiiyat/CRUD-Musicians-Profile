from django.urls import path
from . import views

urlpatterns = [
    path("auth/register/", views.register, name="register"),
    path("auth/login/", views.userLogin, name="login"),
    path("auth/editprofile/", views.editProfile, name="editprofile"),
    path("auth/changepassword/", views.chngPassword, name="changepassword"),
    path("", views.profiles, name="profile"),
    path("auth/logout/", views.userLogout, name="logout"),
]
