from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy


class register(CreateView):
    form_class = forms.userRegistration
    template_name = "register.html"
    success_url = reverse_lazy("register")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "Register"
        return context

    def form_valid(self, form):
        # Add success message correctly
        messages.success(self.request, "Account Created Successfully")
        return super().form_valid(form)


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
                    messages.success(request, "Logged in Successfully")
                    form = login(request, user)
                    return redirect("profile")
            messages.warning(request, "Invalid Username or Password")
        else:
            form = AuthenticationForm()
        return render(request, "register.html", {"page": page, "form": form})


def profiles(request):
    if request.user.is_authenticated:
        page = "Profile"
        profile_data = User.objects.get(username=request.user)

        return render(request, "profile.html", {"page": page, "data": profile_data})
    else:
        return redirect("login")


def editProfile(request):
    page = "Edit Profile"
    if request.user.is_authenticated:
        if request.method == "POST":
            user_form = forms.editProfile(request.POST, instance=request.user)
            if user_form.is_valid():
                messages.success(request, "Profile Updated Successfull")
                user_form.save()
                return redirect("profile")
        else:
            user_form = forms.editProfile(instance=request.user)
        return render(request, "editProfile.html", {"form": user_form, "page": page})

    else:
        return redirect("login")


def chngPassword(request):
    page = "Change Password"
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                messages.success(request, "Successfully Password Updated")
                update_session_auth_hash(request, request.user)
                form.save()
        else:
            form = PasswordChangeForm(request.user)
        return render(request, "passchng.html", {"form": form})
    else:
        return redirect("login")


def userLogout(request):
    if request.user.is_authenticated:
        messages.success(request, "Logged Out Successfull")
        logout(request)
        return redirect("home")
    else:
        return redirect("login")
