from rest_framework import viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .models import Schedule
from .serializers import ScheduleSerializator
from users.permissions import APIKeyPermission
from .filters import ScheduleFilter

class ScheduleViewSet(viewsets.ModelViewSet):
    
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializator
    http_method_names = ['get']
    permission_classes = [APIKeyPermission]
    
    filter_backends = [DjangoFilterBackend]
    filterset_class = ScheduleFilter
    