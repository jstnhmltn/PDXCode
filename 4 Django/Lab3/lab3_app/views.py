from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html', context={})

def redirect(request):
    return render(request, 'redirect.html')

def save_url(request):