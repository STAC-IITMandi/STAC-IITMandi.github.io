from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path("", views.home, name="stac-home"),
    path("astrax", views.astrax, name="astrax"),
    path("zenith", views.zenith, name="zenith"),
    path("utkarsh", views.utkarsh, name="utkarsh"),
    path("about", views.about, name="about"),
    path("alumni", views.alumni, name="alumni"),
    path("photogallery", views.photogallery_, name="photogallery"),
    path("videogallery", views.videogallery_, name="videogallery"),
    path("team", views.team, name="team"),
    path("pleiades", views.pleiades, name="pleiades"),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain")
    ),
    path(
        "sitemap.xml",
        TemplateView.as_view(template_name="sitemap.xml", content_type="text/xml")
    ),
    path("iau", views.iau, name="iau"),
    path("farewell", views.farewell, name="farewell")
]
