from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Upload

# Create your views here.
def showcase_index(request):
    p1 = Upload.objects.all()
    context = {"upload": upload}
    return render(request, "showcase_index.html", context)


def showcase_detail(request, pk):
    upload = Upload.objects.get(pk=pk)
    context = {"upload": upload}
    return render(request, "showcase_detail.html", context)