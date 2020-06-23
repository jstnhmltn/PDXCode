from django.urls import path
from . import views

urlpatterns = [
    path('showcase/', views.showcase_index, name='showcase_index'),
    path('showcase/<int:pk>/', views.showcase_detail, name='showcase_detail'),
]