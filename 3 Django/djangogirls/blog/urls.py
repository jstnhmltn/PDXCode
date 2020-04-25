from django.urls import path
from . import views

# still working
# getting an error after manage.py runserver
# because the view is created yet

urlpatterns = [
    path('', views.post_list, name='post_list'),
]