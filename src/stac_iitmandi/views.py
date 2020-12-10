from django.shortcuts import render
from .models import core_team as members
from .models import coordinators


# rendering home page
def home(request):
    return render(
        request, "stac_iitmandi/home.html", {"title": "Home", "home": "active"}
    )


# rendering template page
def template(request):
    return render(request, "stac_iitmandi/template.html")


# rendering ASTRAX page
def astrax(request):
    return render(
        request,
        "stac_iitmandi/astrax.html",
        {"title": "Astrax", "astrax": "active", "events_": "active"},
    )


# rendering Utkarsh page
def utkarsh(request):
    return render(
        request,
        "stac_iitmandi/utkarsh.html",
        {"title": "Utkarsh", "utkarsh": "active", "events_": "active"},
    )


# rendering Zenith page
def zenith(request):
    return render(
        request,
        "stac_iitmandi/zenith.html",
        {"title": "Zenith", "zenith": "active", "events_": "active"},
    )


# rendering Alumni page
def alumni(request):
    return render(
        request,
        "stac_iitmandi/alumni.html",
        {"title": "Alumni", "alumni": "active"}
    )


# rendering About page
def about(request):
    return render(
        request,
        "stac_iitmandi/about.html",
        {"title": "About", "about": "active"}
    )


# rendering Photogallery page
def photogallery(request):
    return render(
        request,
        "stac_iitmandi/photogallery.html",
        {"title": "Photos", "photos": "active", "gallery_": "active"},
    )


# rendering videogallery page
def videogallery(request):
    return render(
        request,
        "stac_iitmandi/videogallery.html",
        {"title": "Videos", "videos": "active", "gallery_": "active"},
    )


# rendering team page
def team(request):
    context_ = {
        "members": members.objects.all().order_by("batch"),
        "coordinators": coordinators.objects.all().order_by("batch"),
        "title": "Team",
        "team": "active",
    }
    return render(request, "stac_iitmandi/team.html", context_)
