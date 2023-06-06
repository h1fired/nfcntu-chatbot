from typing import Iterable, Optional
from django.db import models
from django.utils import timezone
from django_resized import ResizedImageField
from .telegram import send_broadcast_message

class Announcement(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=4096)
    preview = ResizedImageField(size=[1280, None], upload_to='announcement/', force_format='WEBP', quality=80, blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
