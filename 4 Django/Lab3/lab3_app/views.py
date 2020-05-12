from django.shortcuts import render, redirect
from .models import Shorten

def index(request):
    if request.method == "POST":
        print()
    else:
        short_url = Shorten.objects.all()
    return render(request, 'index.html', context={})

def get_slug():
    pass
