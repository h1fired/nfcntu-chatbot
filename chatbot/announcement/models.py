from django.db import models
from django.utils import timezone


class Announcement(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=4096)
    create_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
