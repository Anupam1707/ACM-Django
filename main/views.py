from django.shortcuts import render
from .models import Event, TeamMember, SocialLink

def index(request):
    social_links = SocialLink.objects.all()
    context = {
        'social_links': social_links,
    }
    return render(request, 'home.html', context)

def home(request):
    social_links = SocialLink.objects.all()
    context = {
        'social_links': social_links,
    }
    return render(request, 'home.html', context)

def about(request):
    social_links = SocialLink.objects.all()
    context = {
        'social_links': social_links,
    }
    return render(request, 'about.html', context)

def events(request):
    events = Event.objects.all()
    social_links = SocialLink.objects.all()
    context = {
        'events': events,
        'social_links': social_links,
    }
    return render(request, 'events.html', context)

def team(request):
    faculty_coordinators = TeamMember.objects.filter(team='Faculty Coordinators')
    acm_team = TeamMember.objects.filter(team='ACM')
    acmw_team = TeamMember.objects.filter(team='ACMW')
    leads_team = TeamMember.objects.filter(team='LEADS')
    social_links = SocialLink.objects.all()
    context = {
        'faculty_coordinators': faculty_coordinators,
        'acm_team': acm_team,
        'acmw_team': acmw_team,
        'leads_team': leads_team,
        'social_links': social_links,
    }
    return render(request, 'team.html', context)