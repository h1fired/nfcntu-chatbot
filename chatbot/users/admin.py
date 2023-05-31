from django.contrib import admin
from .models import UserProfile, Group, Specialty

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialty', 'course_num')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'social_id', 'username', 'first_name', 'last_name', 'group', 'create_date')
