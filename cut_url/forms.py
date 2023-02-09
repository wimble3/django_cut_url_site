from django import forms
from .models import *


class AddShortUrl(forms.ModelForm):
    class Meta:
        model = ShortUrl
        fields = ('url',)
