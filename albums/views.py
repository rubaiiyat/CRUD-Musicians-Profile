from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import albumModel

from django.contrib.auth.decorators import login_required


class addAlbum(CreateView):
    form_class = forms.albumForm
    template_name = "addAlbum.html"
    success_url = reverse_lazy("addalbum")

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
    form_class = forms.albumForm
    template_name = "showAlbum.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "Show Album"

        context["data"] = albumModel.objects.select_related("artist__userprofile").all()

        return context


def editAlbum(request, id):
    if request.user.is_authenticated:
        page = "Edit Album"
        post = get_object_or_404(albumModel, pk=id)
        form = forms.albumForm(instance=post)
        if request.method == "POST":
            form = forms.albumForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, "Updated Successfull")
                return redirect("album")
        else:
            form = forms.albumForm(instance=post)
        return render(request, "editAlbum.html", {"page": page, "form": form})
    else:
        return redirect("login")


def deleteAlbum(request, id):

    if request.user.is_authenticated:
        post = get_object_or_404(albumModel, pk=id)
        post.delete()
        return redirect("album")
    else:
        return redirect("login")
