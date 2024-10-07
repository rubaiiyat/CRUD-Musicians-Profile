from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class userRegistration(UserCreationForm):
    instrument = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=11, required=False)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "instrument",
            "phone",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                instrument=self.cleaned_data["instrument"],
                phone=self.cleaned_data["phone"],
            )
        return user


class editProfile(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
