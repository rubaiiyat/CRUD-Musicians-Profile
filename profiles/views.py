from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    if request.user.is_authenticated:
        return redirect("profile")
    else:
        page = "Register"
        if request.method == "POST":
            form = forms.userRegistration(request.POST)
            if form.is_valid():
                form.save()
                return redirect("register")
        else:
            form = forms.userRegistration()
        return render(request, "register.html", {"page": page, "form": form})


def userLogin(request):
    if request.user.is_authenticated:
        return redirect("profile")
    else:
        page = "Login"
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data.get("username")
                userPass = form.cleaned_data.get("password")
                user = authenticate(request, username=name, password=userPass)
                if user is not None:
                    form = login(request, user)
                    return redirect("profile")
        else:
            form = AuthenticationForm()
        return render(request, "register.html", {"page": page, "form": form})


def profiles(request):
    page = "Profile"
    return render(request, "profile.html", {"page": page})


def userLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("home")
    else:
        return redirect("login")
