from django.shortcuts import render, redirect
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

@ login_required
def showcase_post(request):
    if request.method == 'GET':
        return render(request, 'showcase_post.html')
    elif request.method == 'POST':
        upload = Upload.objects.create()
        context = {'upload': upload}
        return render(request, 'showcase_index.html', context)





#     @login_required
# def add_todo(request):
#     if request.method == 'GET':
#         return render(request, 'todos/add.html')
#     elif request.method == 'POST':
#         title = request.POST['title']
#         text = request.POST['text']
#         if (request.POST['status'] == 'False'):
#             status = False
#         else:
#             status = True
#         todo = Todo.objects.create(
#             title = title, 
#             text = text, 
#             status = status,
#             user = request.user
#         )
#         return redirect('list')