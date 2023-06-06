from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Announcement
from .telegram import send_broadcast_message
from django.contrib import messages



@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'create_date', 'is_published')
    actions = ['send_announcement']
    
    @admin.action(description='Publish selected announcements')
    def send_announcement(self, request, queryset):
        for announcement in queryset:
            if announcement.is_published is not True:
                send_broadcast_message(announcement)
                announcement.is_published=True
                announcement.save()
            else:
                messages.error(request, f'Announcement with id={announcement.id} is already published!')