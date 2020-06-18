from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Upload

# Create your views here.
def showcase_index(request):
    project = Upload.objects.all()
    context = {"projects": project}
    return render(request, "showcase_index.html", context)


def showcase_detail(request, pk):
    project = Upload.objects.get(pk=pk)
    context = {"project": project}
    return render(request, "showcase_detail.html", context)