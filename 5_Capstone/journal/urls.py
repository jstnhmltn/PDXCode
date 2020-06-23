from django.urls import path
from . import views

urlpatterns = [
    path('journal/', views.journal_index, name='journal_index'),
    path('journal/<int:pk>/', views.journal_detail, name='journal_detail'),
]