from rest_framework import serializers
from users.models import UserProfile
from contacts.models import Contact

class UserProfileSerializator(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        
class ContactSerializator(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'