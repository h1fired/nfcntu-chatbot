from rest_framework import serializers
from schedule.models import Schedule


class ScheduleSerializator(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'