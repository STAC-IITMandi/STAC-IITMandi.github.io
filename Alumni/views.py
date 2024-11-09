from django.shortcuts import render
from .models import Alumni
# Create your views here.
def alumni(request):
    alumni = Alumni.objects.all()
    return render(request, 'alumni.html',{'alumni':alumni})