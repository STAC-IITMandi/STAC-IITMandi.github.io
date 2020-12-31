from django.shortcuts import render
from .models import core_team as members
from .models import coordinators, club_activity, homepage, zenithEvents, utkarshEvents


# rendering home page
def home(request):
    introduction = homepage.objects.filter(id__in=(15,))
    context_ = {
        "club_activity": club_activity.objects.all(),
        "competitions": homepage.objects.filter(id__in=(1, 2, 3, 4, 8)),
        "events_intro": homepage.objects.filter(id__in=(6, 5, 7)),
        "future_projects": homepage.objects.filter(id__in=(11, 10, 9, 12, 13, 14)),
        "introduction": introduction[0].description,
        "title": "Home",
        "home": "active",
    }
    return render(request, "stac_iitmandi/home.html", context_)


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
    context_ = {
        "events": utkarshEvents.objects.all(),
        "title": "Utkarsh",
        "utkarsh": "active",
        "events_": "active"
    }
    return render(request, "stac_iitmandi/utkarsh.html", context_)


# rendering Zenith page
def zenith(request):
    context_ = {
        "events": zenithEvents.objects.all(),
        "title": "Zenith",
        "zenith": "active",
        "events_": "active"
    }
    return render(request, "stac_iitmandi/zenith.html", context_)


# rendering Alumni page
def alumni(request):
    return render(
        request, "stac_iitmandi/alumni.html", {"title": "Alumni", "alumni": "active"}
    )


# rendering About page
def about(request):
    return render(
        request, "stac_iitmandi/about.html", {"title": "About", "about": "active"}
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
        "first": members.objects.filter(id__in=(40, 42, 41)),
        "second":members.objects.filter(id__in=(3, 1, 7, 4, 5, 10, 6, 12 ,11, 9, 13, 14 ,15, 21, 22)),
        "third": members.objects.filter(id__in=(20,30, 38, 33, 29, 39, 36, 37, 28, 26, 25, 24, 32, 31, 34, 35)),
        "last":members.objects.filter(id__in=(16, 8,17,18,27)),
        
        "coordinators": coordinators.objects.all().order_by("batch"),
        "title": "Team",
        "team": "active",
    }
    return render(request, "stac_iitmandi/team.html", context_)


"""40, 42, 41, 3, 1, 7, 4, 5, 10, 6, 12 ,11, 9, 13, 14 ,15, 21, 22, 20,30, 38, 33, 29, 39, 36, 37, 28, 26, 25, 24, 32, 31, 34, 35,16, 8,17,18,27"""