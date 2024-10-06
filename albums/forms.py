from . import models
from django import forms


class albumForm(forms.ModelForm):
    class Meta:
        model = models.albumModel
        fields = ["albumName", "artist", "date", "rating"]
