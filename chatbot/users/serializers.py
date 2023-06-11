from rest_framework import serializers
from users.models import UserProfile, Specialty, Group


class UserProfileSerializator(serializers.ModelSerializer):
    
    group = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field='name')
    specialty = serializers.CharField(source='group.specialty.name', allow_blank=True, allow_null=True, read_only=True)
    course_num = serializers.IntegerField(source='group.course_num', allow_null=True, read_only=True)
    
    class Meta:
        model = UserProfile
        fields = '__all__'
        
class GroupSerializator(serializers.ModelSerializer):
    
    specialty = serializers.CharField(source='specialty.name')
    
    class Meta:
        model = Group
        fields = '__all__'
        
class SpecialtySerializator(serializers.ModelSerializer):
    
    class Meta:
        model = Specialty
        fields = '__all__'