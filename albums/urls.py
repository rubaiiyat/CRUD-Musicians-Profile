from django.urls import path, include
from . import views

urlpatterns = [
    path("auth/addAlbum/", views.addAlbum.as_view(), name="addalbum"),
    path("auth/addAlbum/editalbum/<int:id>", views.editAlbum, name="editalbum"),
    path("auth/addAlbum/delete/<int:id>", views.deleteAlbum, name="delete"),
    path("", views.showAlbum.as_view(), name="album"),
]
