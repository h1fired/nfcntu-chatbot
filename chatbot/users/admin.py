from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'social_id', 'username', 'specialty', 'group', 'course_num', 'create_date')
