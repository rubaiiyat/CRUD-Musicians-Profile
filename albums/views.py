from django.shortcuts import render


def album(request):
    page = "Album"
    return render(request, "album.html", {"page": page})
