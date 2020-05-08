from django.db import models
from django.conf.urls import url

class Short(models.Model):
    long_url = models.CharField(max_length=200)
