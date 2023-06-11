from typing import Iterable, Optional
from django.db import models
from users.models import UserProfile

class FAQ(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    question = models.CharField(max_length=256)
    answer = models.TextField(max_length=2048, null=True, blank=True, help_text='Note: After submission, the answer field will not be editable.')
    is_sent = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.question)
    