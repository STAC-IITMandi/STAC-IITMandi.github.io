from django.shortcuts import render

def home(request):
    return render(request, 'stac_iitmandi/home.html')

def template(request):
    return render(request, 'stac_iitmandi/template.html')