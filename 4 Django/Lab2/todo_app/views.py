from django.shortcuts import render, redirect
from .models import Todo

from django.http import HttpResponse


def index(request):
    tasks = Todo.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'main/index.html', context=context)