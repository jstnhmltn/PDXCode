from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html', context={})

def save_url(request):
    return render(request, 'save_url.html')