from django.http import HttpResponse
from django.shortcuts import render
from HomePage import views
from HomePage.models import Projects,ClubActivity,Achievements,Fests
# Create your views here.
def homepage(request):
    content={
        'projects':Projects.objects.all(),
        'clubactivity':ClubActivity.objects.all(),
        'achievements': Achievements.objects.all(),
        'fests': Fests.objects.all(),
    }
    return render(request, 'home.html' ,{'content':content})