import random
from django.shortcuts import render
from django.contrib.auth.models import User


def home(request):
    page = "Home"
    data = User.objects.all()

    for user in data:
        user.count_followers = random.randint(10000, 50000)
        user.count_following = random.randint(10, 300)
    return render(request, "home.html", {"page": page, "data": data})
