from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Upload
from .forms import UploadForm

def showcase_index(request):
    uploads = Upload.objects.all()
    context = {'uploads': uploads}
    return render(request, 'showcase_index.html', context)

def showcase_detail(request, pk):
    upload = Upload.objects.get(pk=pk)
    context = {'upload': upload}
    return render(request, 'showcase_detail.html', context)

# @ login_required
# def showcase_post(request):
#     if request.method == 'GET':
#         return render(request, 'showcase_post.html')
#     elif request.method == 'POST':
#         upload = Upload.objects.create()
#         context = {'upload': upload}
#         return render(request, 'showcase_index.html', context)

@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showcase_index')
    else:
        form = UploadForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })