from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

class Upload(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length = 500)
    upload_date = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    user_image = models.ImageField(null=True)

    def __str__(self):
        return self.title



    