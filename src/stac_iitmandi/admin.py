from django.contrib import admin
from .models import core_team, coordinators, club_activity, homepage

# register models
admin.site.register(core_team)
admin.site.register(coordinators)
admin.site.register(club_activity)
admin.site.register(homepage)
