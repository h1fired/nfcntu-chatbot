from django.db import models
from django.utils import timezone

class UserProfile(models.Model):
    social_id = models.PositiveIntegerField(unique=True, verbose_name='ID користувача в телеграмі')
    username = models.CharField(max_length=128, verbose_name='Нік користувача')
    first_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='Ім\'я користувача')
    last_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='Прізвище користувача')
    specialty = models.CharField(max_length=128, blank=True, null=True, verbose_name='Спеціальність студента')
    course_num = models.PositiveIntegerField(blank=True, null=True, verbose_name='Курс студента')
    group = models.CharField(blank=True, null=True, max_length=16, verbose_name='Група студента')
    create_date = models.DateTimeField(default=timezone.now, verbose_name='Дата створення профілю', editable=False)
        
    def __str__(self):
        return self.username
