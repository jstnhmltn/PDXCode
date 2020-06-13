from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pages/', views.contact, name='contact'),
    path('pages/', views.register, name='register'),
]