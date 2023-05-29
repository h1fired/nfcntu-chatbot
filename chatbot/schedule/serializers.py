from rest_framework import serializers
from schedule.models import Schedule


class ScheduleSerializator(serializers.ModelSerializer):
    group = serializers.CharField(source='group.name', allow_blank=True, allow_null=True)
    
    class Meta:
        model = Schedule
        fields = '__all__'