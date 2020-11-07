from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='stac-home'),
    path('template.html', views.template, name='template'),
    path('astrax.html', views.astrax, name = 'astrax'),
    path('zenith.html', views.zenith, name = 'zenith'),
    path('utkarsh.html', views.utkarsh, name = 'utkarsh'),
    path('about.html', views.about, name = 'about'),
    path('alumni_s.html', views.alumni_s, name = 'alumni_s'),
    path('photogallery.html', views.photogallery, name = 'photogallery'),
    path('videogallery.html', views.videogallery, name = 'videogallery'),
]