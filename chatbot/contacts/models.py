from django.db import models

class Contact(models.Model):
    GROUPS = [
        ('Administration', 'Адміністрація'),
        ('Practice', 'Практика'),
        ('Introduction', 'Вступ'),
    ]
    
    name = models.CharField(max_length=128, unique=True)
    contact = models.CharField(max_length=128)
    group = models.CharField(max_length=128, choices=GROUPS)
    
    def __str__(self):
        return self.name
    