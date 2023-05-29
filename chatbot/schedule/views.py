from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from .models import Schedule
from users.models import Group
from .serializers import ScheduleSerializator
from users.permissions import APIKeyPermission

class ScheduleViewSet(viewsets.ViewSet):
    
    http_method_names = ['get']
    permission_classes = [APIKeyPermission]
    
    def list(self, request):
        schedules = Schedule.objects.all()
        serialized_schedule = ScheduleSerializator(schedules, many=True)
        return Response(serialized_schedule.data)
        
    # get schedule by group
    @action(detail=False, methods=['get'], url_path='(?P<group>[^/.]+)', url_name='group')
    def get_group_schedule(self, request, group=None):
        if Group.objects.filter(name=group).exists() is not True:
            raise NotFound('Group does not exists.')
        group_obj = Group.objects.get(name=group)
        group_schedules = Schedule.objects.filter(group=group_obj)
        serializer = ScheduleSerializator(group_schedules, many=True)
        return Response(serializer.data)
    