from django.db import models

class User(models.Model):
    firt_name = models.CharField(max_length=75)
    last_name = models.Charfield(max_length=75)
    