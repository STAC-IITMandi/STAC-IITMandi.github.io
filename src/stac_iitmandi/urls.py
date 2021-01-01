from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="stac-home"),
    path("astrax", views.astrax, name="astrax"),
    path("zenith", views.zenith, name="zenith"),
    path("utkarsh", views.utkarsh, name="utkarsh"),
    path("about", views.about, name="about"),
    path("alumni", views.alumni, name="alumni"),
    path("photogallery", views.photogallery, name="photogallery"),
    path("videogallery", views.videogallery, name="videogallery"),
    path("team", views.team, name="team"),
    path("pleiades", views.pleiades, name="pleiades"),
]
