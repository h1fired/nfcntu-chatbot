from django_filters import rest_framework as filters
from .models import Schedule

class ScheduleFilter(filters.FilterSet):
    group = filters.CharFilter(field_name='group__name')

    class Meta:
        model = Schedule
        fields = ['group', 'day']