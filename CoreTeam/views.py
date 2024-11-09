from django.shortcuts import render
from .models import MemberDetail

def CoreTeam(request):
    team_members = MemberDetail.objects.all()
    members = {
        'a': team_members.filter(position='A'),
        'b': team_members.filter(position='B'),
        'c': team_members.filter(position='C'),
        'd': team_members.filter(position='D'),
    }
    return render(request, 'CoreTeam.html', {'team_member': members})