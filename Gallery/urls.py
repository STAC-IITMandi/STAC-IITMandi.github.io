from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('photogallery', views.photogallery, name='photogallery'),
    path('videogallery', views.videogallery, name='videogallery'),
    path("__reload__", include("django_browser_reload.urls")),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)