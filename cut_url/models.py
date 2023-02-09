from django.db import models


class ShortUrl(models.Model):
    url = models.CharField(max_length=1000)
    short_url = models.CharField(max_length=255, unique=True)
