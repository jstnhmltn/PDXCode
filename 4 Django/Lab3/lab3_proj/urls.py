from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lab3_app')),
    path('', include('save_url.urls')),
    path('', include('redirect.urls'))
]
