from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class userRegistration(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class editProfile(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
