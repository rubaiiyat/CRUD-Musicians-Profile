from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy


class register(CreateView):
    form_class = forms.userRegistration
    template_name = "register.html"
    success_url = reverse_lazy("register")

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("profile")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "Register"
        return context

    def form_valid(self, form):
        # Add success message correctly
        messages.success(self.request, "Account Created Successfully")
        return super().form_valid(form)


class userLogin(LoginView):
    template_name = "register.html"

    def dispatch(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:
            return redirect("profile")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self) -> str:
        return reverse_lazy("profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "Login"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Logged in Successfully")

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Invalid Username or Password")
        return super().form_invalid(form)


class profiles(TemplateView):
    template_name = "profile.html"

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "User Profile"
        context["data"] = self.request.user
        return context


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


class chngPassword(PasswordChangeView):
    template_name = "passchng.html"

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "Change Password"
        return context

    def get_success_url(self) -> str:
        return reverse_lazy("profile")

    def form_valid(self, form):
        messages.success(self.request, "Updated Your Password")
        return super().form_valid(form)


def userLogout(request):
    if request.user.is_authenticated:
        logout(request)

        return redirect("login")
