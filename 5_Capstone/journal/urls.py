from django.urls import path
from . import views

urlpatterns = [
    path("", views.journal_index, name="journal_index"),
    path("<int:pk>/", views.journal_detail, name="journal_detail"),
]