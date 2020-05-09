from django.db import models
from django.conf.urls import url

def get_absolute_url(self):
    return reverse_lazy('blog_page', args=[self.slug])