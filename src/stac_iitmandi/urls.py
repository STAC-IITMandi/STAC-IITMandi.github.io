from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='stac-home'),
    path('template.html', views.template, name='template'),
]