from django.contrib import admin
from .models import Event, TeamMember, SocialLink

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'event_date')

admin.site.register(Event, EventAdmin)
admin.site.register(TeamMember)
admin.site.register(SocialLink)