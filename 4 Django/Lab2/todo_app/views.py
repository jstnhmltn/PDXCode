from django.shortcuts import render
from todo_app.models import Todo

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")