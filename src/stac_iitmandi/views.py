from django.shortcuts import render


# rendering home page 
def home(request):
    return render(request, 'stac_iitmandi/home.html' , {'title': 'Home'})
# rendering template page
def template(request):
    return render(request, 'stac_iitmandi/template.html')
# rendering ASTRAX page
def astrax(request):
    return render(request, 'stac_iitmandi/astrax.html', {'title': 'Astrax'})
# rendering Utkarsh page
def utkarsh(request):
    return render(request, 'stac_iitmandi/utkarsh.html', {'title': 'Utkarsh'})
# rendering Zenith page
def zenith(request):
    return render(request, 'stac_iitmandi/zenith.html', {'title': 'Zenith'})
# rendering Alumni's page    
def alumni_s(request):
    return render(request, "stac_iitmandi/alumni_s.html", {'title': "Alumni's"})
# rendering About page
def about(request):
    return render(request, 'stac_iitmandi/about.html', {'title': 'About'})
# rendering Photogallery page
def photogallery(request):
    return render(request, 'stac_iitmandi/photogallery.html', {'title': 'Photos'})
#rendering videogallery page
def videogallery(request):
    return render(request, 'stac_iitmandi/videogallery.html', {'title': 'Videos'})