from rest_framework import serializers
from users.models import UserProfile

class UserProfileSerializator(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'