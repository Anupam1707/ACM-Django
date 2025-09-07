from django.db import models
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.CharField(max_length=100) # For display
    event_date = models.DateField(default=timezone.now)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['event_date']

class TeamMember(models.Model):
    TEAM_CHOICES = [
        ('Faculty Coordinators', 'Faculty Coordinators'),
        ('ACM', 'ACM 2025-26'),
        ('ACMW', 'ACM-W 2025-26'),
        ('LEADS', 'LEADS 2025-26'),
    ]
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True, null=True)
    team = models.CharField(max_length=50, choices=TEAM_CHOICES)
    image = models.ImageField(upload_to='team_images/', blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']

class SocialLink(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    icon_class = models.CharField(max_length=100)

    def __str__(self):
        return self.name
