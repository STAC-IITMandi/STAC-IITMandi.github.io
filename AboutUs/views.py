from django.shortcuts import render
from .models import aboutUs

def AboutUs(request):
    aboutus = aboutUs.objects.first()
    return render(request, 'aboutus.html',{'aboutus':aboutus} )