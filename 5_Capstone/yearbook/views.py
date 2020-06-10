from django.shortcuts import render
from django.contrib.auth import HTTPRespnse

from .models import User

# Create your views here.
def home(render):
    return HTTPResponse