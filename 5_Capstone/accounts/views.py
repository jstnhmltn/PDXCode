from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from .forms import SignUpForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('showcase_index')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')

def LoginView(request):
    return render(request, 'login.html')
    
def LogoutView(request):
    return redirect('showcase_index')