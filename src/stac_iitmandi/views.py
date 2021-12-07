from django.shortcuts import render, redirect
from .models import core_team as members
from .models import (
    coordinators,
    club_activity,
    homepage,
    achievements,
    zenithEvents,
    utkarshEvents,
    Astrax,
    About,
    photogallery,
    videogallery,
    Alumni,
    Pleiades,
    Links,
)


# rendering home page
def home(request):
    context_ = {
        "club_activity": club_activity.objects.all(),
        "competitions": homepage.objects.filter(id__in=(1, 2, 3, 4, 8)),
        "events_intro": homepage.objects.filter(id__in=(6, 5, 7)),
        "future_projects": homepage.objects.filter(id__in=(11, 10, 9, 12, 13, 14)),
        "introduction": homepage.objects.get(id__in=(15,)),
        "home": "active",
        "achievements": achievements.objects.all(),
        # "astrax": Links.objects.ffilter(linkname="astrax"),
        # "pleiades": Links.objects.filter(linkname="pleiades"),
        # "utkarsh": Links.objects.filter(linkname="utkarsh"),
        # "zenith": Links.objects.filter(linkname="zenith"),
        "links": Links.objects.all(),
    }
    return render(request, "stac_iitmandi/home.html", context_)


# rendering ASTRAX page
def astrax(request):
    """ context_ = {
        "events": Astrax.objects.all().exclude(id__in=(6, 1, 2, 3, 4)).order_by("-id"),
        "about_astrax": Astrax.objects.filter(id__in=(1, 2, 3, 4)).order_by("-id"),
        "title": "Astrax",
        "astrax": "active",
        "events_": "active",
        "astrax_intro": homepage.objects.get(id__in=(6,)),
    }
    return render(request, "stac_iitmandi/astrax.html", context_) """
    return redirect('https://astrax.in/')


# rendering Utkarsh page
def utkarsh(request):
    context_ = {
        "events": utkarshEvents.objects.all().exclude(id__in=(4,)).order_by("-id"),
        "title": "Utkarsh",
        "utkarsh": "active",
        "events_": "active",
        "utkarsh_intro": utkarshEvents.objects.get(id__in=(4,)),
    }
    return render(request, "stac_iitmandi/utkarsh.html", context_)


# rendering Zenith page
def zenith(request):
    context_ = {
        "events": zenithEvents.objects.all().exclude(id__in=(10,)).order_by("-id"),
        "title": "Zenith",
        "zenith": "active",
        "events_": "active",
        "zenith_intro": zenithEvents.objects.get(id__in=(10,)),
    }
    return render(request, "stac_iitmandi/zenith.html", context_)


# rendering pleiades page
def pleiades(request):
    context_ = {
        "events": Pleiades.objects.all().exclude(id__in=(1,)).order_by("-id"),
        "title": "Pleiades",
        "pleiades": "active",
        "events_": "active",
        "pleiades_intro": Pleiades.objects.get(id__in=(1,)),
    }
    return render(request, "stac_iitmandi/pleiades.html", context_)


# rendering Alumni page
def alumni(request):
    context_ = {
        "Alumni_s": Alumni.objects.all(),
        "title": "Alumni",
        "alumni": "active",
    }
    return render(request, "stac_iitmandi/alumni.html", context_)


# rendering About page
def about(request):
    context_ = {
        "title": "About",
        "about": "active",
        "about_intro": About.objects.get(id__in=(1,)),
    }
    return render(request, "stac_iitmandi/about.html", context_)


# rendering Photogallery page
def photogallery_(request):
    context_ = {
        "photogallery": photogallery.objects.all().order_by("-id"),
        "title": "Photos",
        "photos": "active",
        "gallery_": "active",
    }
    return render(request, "stac_iitmandi/photogallery.html", context_)


# rendering videogallery page
def videogallery_(request):
    context_ = {
        "videogallery": videogallery.objects.all().order_by("-id"),
        "title": "Videos",
        "videos": "active",
        "gallery_": "active",
    }
    return render(request, "stac_iitmandi/videogallery.html", context_)


# rendering team page
def team(request):
    context_ = {
        "lead": members.objects.all().filter(
            id__in=(53, 51)),
        "opensource_and_webdev": members.objects.all().filter(
            id__in=(43, 45, 47, 52)),
        "astrophotography_and_equipment": members.objects.all().filter(
            id__in=(56, 46, 54, 43)),
        "sciencecommunication_and_outreach": members.objects.all().filter(
            id__in=(48, 49, 50, 51, 52, 54, 56)),
        "media": members.objects.all().filter(
            id__in=(44, 45, 46, 49, 47, 55)),
        "title": "Team",
        "team": "active",
    }
    return render(request, "stac_iitmandi/team.html", context_)


# rendering IAU page
def iau(request):
    context_ = {
        "title": "IAU",
        "about": "active",
        # "IAU_intro": IAU.objects.get(id__in=(1,)),
    }
    return render(request, "stac_iitmandi/iau.html", context_)


def farewell(request):
    return render(request, "stac_iitmandi/farewell.html")
