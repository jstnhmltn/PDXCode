from django.shortcuts import render
from django.conf import urls
from . import views

def home(request):
    return render(request, 'home.html')