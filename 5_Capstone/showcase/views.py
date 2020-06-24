from django.shortcuts import render

from .models import Upload

    
def showcase_index(request):
    uploads = Upload.objects.all()
    context = {'uploads': uploads}
    return render(request, 'showcase_index.html', context)

def showcase_detail(request, pk):
    upload = Upload.objects.get(pk=pk)
    context = {'upload': upload}
    return render(request, 'showcase_detail.html', context)

def showcase_post():
    pass