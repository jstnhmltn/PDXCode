from django.urls import path
from . import views

urlpatterns = [
    path('', views.showcase_index, name='showcase_index'),
    path('<int:pk>/', views.showcase_detail, name='showcase_detail'),
    path('showcase/', views.model_form_upload, name='model_form_upload'),
    # path('showcase/', views.showcase_post, name='showcase_post'),
]