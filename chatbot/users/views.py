from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import UserProfile, Group, Specialty
from .serializers import UserProfileSerializator, GroupSerializator, SpecialtySerializator
from .permissions import APIKeyPermission

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializator
    http_method_names = ['get', 'post', 'put', 'patch']
    lookup_field = 'social_id'
    permission_classes = [APIKeyPermission]
    

class SpecialtyViewset(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializator
    http_method_names = ['get']
    permission_classes = [APIKeyPermission]
    
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializator
    http_method_names = ['get']
    permission_classes = [APIKeyPermission]