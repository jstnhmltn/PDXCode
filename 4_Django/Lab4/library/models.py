from django.db import models

from datetime import datetime

    
class Book(models.Model):
    title = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)

class Author(models.Model):
    name = models.CharField(max_length=50)