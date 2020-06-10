from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/pages/', view.about, name='about'),
    path('/pages/', views.contact, name='contact)',
    path('/pages/', view.news, name='news'),
]