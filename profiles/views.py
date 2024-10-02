from django.shortcuts import render


def register(request):
    page = "Register"
    return render(request, "register.html", {"page": page})


def userLogin(request):
    page = "Login"
    return render(request, "register.html", {"page": page})


def profiles(request):
    page = "Profile"
    return render(request, "profile.html", {"page": page})
