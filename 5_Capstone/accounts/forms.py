from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, required=True, help_text='*Required')
    username = forms.CharField(max_length=30, required=True, help_text='*Required')
    location = forms.CharField(max_length=50, required=False, help_text='Optional')
    birthdate = forms.DateField(widget=forms.SelectDateWidget, required=False, help_text='Optional')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'location', 'password1', 'password2', )

# class LogInForm(user.Users):
#     username = forms.CharField(max_length=)
#     password1 = 

#     class Meta:
#         model = User
#         fields = ('username', 'password1')
