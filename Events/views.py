from django.shortcuts import render
from .models import Astrax, Pleiades, Zenith, Utkarsh

# Create your views here.
def astrax(request):
    astrax = Astrax.objects.all()
    return render(request, 'astrax.html',{'astrax':astrax})

def pleiades(request):
    pleiades = Pleiades.objects.all()
    return render(request, 'pleiades.html',{'pleiades':pleiades})

def zenith(request):
    zenith = Zenith.objects.all()
    return render(request, 'zenith.html',{'zenith':zenith})

def utkarsh(request):
    utkarsh = Utkarsh.objects.all()
    return render(request, 'utkarsh.html',{'utkarsh':utkarsh})