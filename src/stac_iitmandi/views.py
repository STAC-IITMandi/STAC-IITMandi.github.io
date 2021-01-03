from django.shortcuts import render
from .models import core_team as members
from .models import (
    coordinators,
    club_activity,
    homepage,
    achievements,
    zenithEvents,
    utkarshEvents,
    # Astrax,
    About,
    photogallery,
    videogallery,
    Alumni,
    Pleiades,
    Links,
)


# rendering home page
def home(request):
    introduction = homepage.objects.filter(id__in=(15,))
    context_ = {
        "club_activity": club_activity.objects.all(),
        "competitions": homepage.objects.filter(id__in=(1, 2, 3, 4, 8)),
        "events_intro": homepage.objects.filter(id__in=(6, 5, 7)),
        "future_projects": homepage.objects.filter(id__in=(11, 10, 9, 12, 13, 14)),
        "introduction": introduction[0].description,
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
    astrax_intro = homepage.objects.filter(id__in=(6,))
    context_ = {
        # "events": Astrax.objects.all().exclude(id__in=(6,)),
        "title": "Astrax",
        "astrax": "active",
        "events_": "active",
        "astrax_intro": astrax_intro[0].description,
    }
    return render(request, "stac_iitmandi/astrax.html", context_)


# rendering Utkarsh page
def utkarsh(request):
    utkarsh_intro = utkarshEvents.objects.filter(id__in=(4,))
    context_ = {
        "events": utkarshEvents.objects.all().exclude(id__in=(4,)).order_by("-id"),
        "title": "Utkarsh",
        "utkarsh": "active",
        "events_": "active",
        "utkarsh_intro": utkarsh_intro[0].description,
    }
    return render(request, "stac_iitmandi/utkarsh.html", context_)


# rendering Zenith page
def zenith(request):
    zenith_intro = zenithEvents.objects.filter(id__in=(10,))
    context_ = {
        "events": zenithEvents.objects.all().exclude(id__in=(10,)).order_by("-id"),
        "title": "Zenith",
        "zenith": "active",
        "events_": "active",
        "zenith_intro": zenith_intro[0].description,
    }
    return render(request, "stac_iitmandi/zenith.html", context_)


# rendering pleiades page
def pleiades(request):
    pleiades_intro = Pleiades.objects.filter(id__in=(1,))
    context_ = {
        "events": Pleiades.objects.all().exclude(id__in=(1,)).order_by("-id"),
        "title": "Pleiades",
        "pleiades": "active",
        "events_": "active",
        "pleiades_intro": pleiades_intro[0].description,
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
    about_intro = About.objects.filter(id__in=(1,))
    context_ = {
        "title": "About",
        "about": "active",
        "about_intro": about_intro[0].description,
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
        "first": members.objects.filter(id__in=(40, 42, 41)),
        "second": members.objects.filter(
            id__in=(3, 1, 7, 4, 5, 10, 6, 12, 11, 9, 13, 14, 15, 21, 22)
        ),
        "third": members.objects.filter(
            id__in=(20, 30, 38, 33, 29, 39, 36, 37, 28, 26, 25, 24, 32, 31, 34, 35)
        ),
        "last": members.objects.filter(id__in=(16, 8, 17, 18, 27)),
        "new": members.objects.all().exclude(
            id__in=[
                40,
                42,
                41,
                3,
                1,
                7,
                4,
                5,
                10,
                6,
                12,
                11,
                9,
                13,
                14,
                15,
                21,
                22,
                20,
                30,
                38,
                33,
                29,
                39,
                36,
                37,
                28,
                26,
                25,
                24,
                32,
                31,
                34,
                35,
                16,
                8,
                17,
                18,
                27,
            ]
        ),
        "coordinators": coordinators.objects.all().order_by("batch"),
        "title": "Team",
        "team": "active",
    }
    return render(request, "stac_iitmandi/team.html", context_)


# "members": members.objects.filter(id__in=[40, 42, 41, 3, 1, 7, 4, 5, 10, 6, 12, 11, 9, 13, 14, 15, 21, 22, 20, 30, 38, 33, 29, 39, 36, 37, 28, 26, 25, 24, 32, 31, 34, 35, 16, 8, 17, 18, 27]),
