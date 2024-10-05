from django.urls import path
from . import views

urlpatterns = [
    path("auth/register/", views.register.as_view(), name="register"),
    path("auth/login/", views.userLogin.as_view(), name="login"),
    path("auth/editprofile/", views.editProfile, name="editprofile"),
    path("auth/changepassword/", views.chngPassword, name="changepassword"),
    path("", views.profiles.as_view(), name="profile"),
    path("auth/logout/", views.userLogout, name="logout"),
]
