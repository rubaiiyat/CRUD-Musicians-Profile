from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class albumModel(models.Model):
    select = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]

    albumName = models.CharField(max_length=100)
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=False)
    rating = models.IntegerField(choices=select, default=5)

    def __str__(self) -> str:
        return f"{self.albumName} by {self.artist}"
