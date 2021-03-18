from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from eruditoapp import views



urlpatterns = [
    path('', include('eruditoapp.urls')),
    path('admin/', admin.site.urls),
]