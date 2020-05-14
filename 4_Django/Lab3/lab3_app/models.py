from django.db import models
from django.conf.urls import url

class Shorten(models.Model):
    long_url = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, verbose_name='URL Slug')