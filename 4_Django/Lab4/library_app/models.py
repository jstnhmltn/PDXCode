from django.db import models

from datetime import datetime

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Book(models.Model):
    title = models.CharField(max_length=50)
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)