from rest_framework import viewsets
from .models import Announcement
from .serializers import AnnouncementSerializator
from users.permissions import APIKeyPermission

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializator
    http_method_names = ['get', 'post']
    permission_classes = [APIKeyPermission]