from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from users.models import UserProfile, Specialty, Group

class UserProfileSerializator(serializers.ModelSerializer):
    
    group = serializers.CharField(source='group.name', allow_blank=True, allow_null=True)
    specialty = serializers.CharField(source='group.specialty.name', allow_blank=True, allow_null=True, read_only=True)
    course_num = serializers.IntegerField(source='group.course_num', allow_null=True, read_only=True)
    
    class Meta:
        model = UserProfile
        fields = '__all__'
        
    def create(self, validated_data):
        group_name = validated_data.pop('group')['name']
        try:
            group_instance = Group.objects.get(name=group_name)
        except:
            raise serializers.ValidationError('Group object does not exists.')
        user_instance = UserProfile.objects.create(group=group_instance, **validated_data)
        return user_instance
    
    
        
        
class GroupSerializator(serializers.ModelSerializer):
    
    specialty = serializers.CharField(source='specialty.name')
    
    class Meta:
        model = Group
        fields = '__all__'
        
class SpecialtySerializator(serializers.ModelSerializer):
    
    class Meta:
        model = Specialty
        fields = '__all__'