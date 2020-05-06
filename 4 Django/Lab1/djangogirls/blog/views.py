from django.shortcuts import render
from django.utils import timezone

def post_list(request):
    return render(request, 'post_list.html', {})