from rest_framework import serializers
from users.models import UserProfile
from contacts.models import Contact

class UserProfileSerializator(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['social_id', 'username', 'specialty', 'course_num', 'group']
        
class ContactSerializator(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'contact', 'group']