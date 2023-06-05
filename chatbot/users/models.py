from django.db import models
from django.utils import timezone


class Specialty(models.Model):
    name = models.CharField(max_length=256, unique=True)
    
    def __str__(self):
        return self.name
    
class Group(models.Model):
    name = models.CharField(max_length=256, unique=True)
    specialty = models.ForeignKey(Specialty, related_name='specialty', on_delete=models.CASCADE)
    course_num = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    social_id = models.PositiveIntegerField(unique=True, verbose_name='ID користувача в телеграмі')
    chat_id = models.PositiveIntegerField(unique=True, verbose_name='ID чату в телеграмі')
    username = models.CharField(max_length=128, verbose_name='Нік користувача')
    first_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='Ім\'я користувача')
    last_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='Прізвище користувача')
    group = models.ForeignKey(Group, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Група студента')
    create_date = models.DateTimeField(default=timezone.now, verbose_name='Дата створення профілю', editable=False)
        
    def __str__(self):
        return self.username
