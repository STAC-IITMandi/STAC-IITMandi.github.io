from django.contrib import admin
from .models import (
    core_team,
    coordinators,
    club_activity,
    homepage,
    zenithEvents,
    utkarshEvents,
    Astrax,
    photogallery,
    About,
    Alumni,
    videogallery,
    Pleiades,
)

# register models
admin.site.register(core_team)
admin.site.register(coordinators)
admin.site.register(club_activity)
admin.site.register(homepage)
admin.site.register(zenithEvents)
admin.site.register(utkarshEvents)
admin.site.register(Astrax)
admin.site.register(photogallery)
admin.site.register(videogallery)
admin.site.register(About)
admin.site.register(Alumni)
admin.site.register(Pleiades)
