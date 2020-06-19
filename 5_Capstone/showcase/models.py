from django.conf import settings
from django.db import models

class Upload(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length = 500)
    upload_date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title
