from django.shortcuts import render
from .models import PhotoGallery, VideoGallery

#rendering Photogallery page
def photogallery(request):
    photo = PhotoGallery.objects.all()
    return render(request, "photogallery.html",{'photo':photo} )

# rendering videogallery page
def videogallery(request):
    video = VideoGallery.objects.all()
    return render(request, "videogallery.html", {"video": video})