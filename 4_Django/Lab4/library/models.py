from django.db import models

from datetime import datetime

    
class Book(models.Model):
    title = models.CharField(max_length=50)
    author_last_name = models.CharField(max_length=30)
    author_first_name = models.CharField(max_length=30)
    is_available = models.BooleanField(default=True)

