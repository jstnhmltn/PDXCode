from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'lab3_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.redirect, name='redirect'),
    path('', views.save_url, name='save_url'),
]