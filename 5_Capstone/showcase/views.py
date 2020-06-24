from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Upload

def showcase_index(request):
    uploads = Upload.objects.all()
    context = {'uploads': uploads}
    return render(request, 'showcase_index.html', context)

def showcase_detail(request, pk):
    upload = Upload.objects.get(pk=pk)
    context = {'upload': upload}
    return render(request, 'showcase_detail.html', context)

# @ login_required
# def showcase_post(request, pk):
#     upload = Upload.objects.new(pk=pk)
#     context = {'upload': upload}
#     return render(request, 'showcase_post.html,')