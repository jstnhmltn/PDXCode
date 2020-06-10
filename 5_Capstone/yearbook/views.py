from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Upload

# Create your views here.
def home(request):
    return render(request, 'home.html', context={})

def about(request):
    pass

def contact(request):
    pass

def news(request):
    pass

def register(request):
    pass