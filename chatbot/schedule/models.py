from django.db import models
from django_jsonform.models.fields import JSONField
from users.models import Group

class Schedule(models.Model):
    DAYS = [
        ('Понеділок', 'Понеділок'),
        ('Вівторок', 'Вівторок'),
        ('Середа', 'Середа'),
        ('Четвер', 'Четвер'),
        ('П\'ятниця', 'П\'ятниця'),
    ]
    
    SUBJECTS_SCHEMA = {
        'type': 'array',
        'items': {
            'type': 'string'
        }
    }
    
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    day = models.CharField(max_length=32, choices=DAYS)
    subjects = JSONField(schema=SUBJECTS_SCHEMA)
    
    class Meta:
        unique_together = ['group', 'day']
