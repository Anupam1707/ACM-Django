from django.shortcuts import render
from .models import Event, TeamMember, SocialLink

def index(request):
    events = Event.objects.all()
    faculty_coordinators = TeamMember.objects.filter(team='Faculty Coordinators')
    acm_team = TeamMember.objects.filter(team='ACM')
    acmw_team = TeamMember.objects.filter(team='ACMW')
    leads_team = TeamMember.objects.filter(team='LEADS')
    social_links = SocialLink.objects.all()

    context = {
        'events': events,
        'faculty_coordinators': faculty_coordinators,
        'acm_team': acm_team,
        'acmw_team': acmw_team,
        'leads_team': leads_team,
        'social_links': social_links,
    }
    return render(request, 'index.html', context)
