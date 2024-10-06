from django.shortcuts import render, redirect
from . import forms
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages


class addAlbum(CreateView):
    form_class = forms.albumForm
    template_name = "addAlbum.html"
    success_url = reverse_lazy("album")

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "Add Album"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Album Added")
        return super().form_valid(form)


class showAlbum(TemplateView):
    template_name = "showAlbum.html"

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "Show Album"
        context["data"] = self.request.user
        return context
