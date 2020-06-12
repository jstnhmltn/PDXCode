from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Upload

# Create your views here.
def index(request):
    return render(request, 'index.html', context={})

def about(request):
    return render(request, 'about.html', context={})

def contact(request):
    return render(request, 'contact.html', context={})

def news(request):
    return render(request, 'news.html', context={})

def register(request):
    return render(request, 'register.html', context={})
