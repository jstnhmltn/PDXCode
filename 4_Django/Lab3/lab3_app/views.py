from django.shortcuts import render, redirect
from .models import Shorten
import random, string

def index(request):
    if request.method == "POST":
        print()
    else:
        short_url = Shorten.objects.all()
    return render(request, 'index.html', context={})

def get_slug(request):
    slug = []
    for i in range(25):
        slug.append(random.choice(string.printable))
    return render(request, 'short.html', context={})
