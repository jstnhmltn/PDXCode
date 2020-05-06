from django.shortcuts import render, redirect
from todo_app.models import Todo

from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')