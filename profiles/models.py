from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    instrument = models.CharField(max_length=50)
    phone = models.CharField(max_length=11, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
