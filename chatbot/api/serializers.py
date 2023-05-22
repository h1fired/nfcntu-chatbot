from rest_framework import serializers
from users.models import UserProfile

class UserProfileSerializator(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['social_id', 'username', 'specialty', 'course_num', 'group']