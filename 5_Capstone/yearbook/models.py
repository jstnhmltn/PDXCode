from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

class Upload(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField(max_length = 500)
    status = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    completed_at = models.DateTimeField(blank = True, null = True)
    task_duration = models.DecimalField(max_digits = 4, decimal_places = 2, blank = True, null = True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    