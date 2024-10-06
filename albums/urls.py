from django.urls import path, include
from . import views

urlpatterns = [
    path("auth/addAlbum/", views.addAlbum.as_view(), name="addalbum"),
    path("", views.showAlbum.as_view(), name="album"),
]
