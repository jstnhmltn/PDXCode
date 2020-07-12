
# urlpatterns = [
#     path('login/', views.login, name='login'),
# ]

from . import views
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import logout, login
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    url('login/$', auth_views.LoginView.as_view(), name='login'),
    url('logout/$', auth_views.LogoutView.as_view(), name='logout'),
    # url('admin/', admin.site.urls),
]