from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html', context={})

def process(request):
    return render(request, 'save_url.html')

def short_url(request):
    return render(request, 'short_url.html')