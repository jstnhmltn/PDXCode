from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.showcase_index, name='showcase_index'),
    path('<int:pk>/', views.showcase_detail, name='showcase_detail'),
]