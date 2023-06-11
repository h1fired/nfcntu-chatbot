from rest_framework import serializers
from .models import FAQ
from users.models import UserProfile
    
class FAQSerializator(serializers.ModelSerializer):
    
    user = serializers.SlugRelatedField(queryset=UserProfile.objects.all(), slug_field='social_id')
    
    class Meta:
        model = FAQ
        fields = ['user', 'question']