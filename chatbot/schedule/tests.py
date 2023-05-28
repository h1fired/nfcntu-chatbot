from rest_framework.test import APITestCase
from rest_framework import status
from django.db import IntegrityError
from django.urls import reverse
from .models import Schedule
from django.conf import settings

# Unique Together test
class UserProfileAPITest(APITestCase):
    
    def setUp(self):
        Schedule.objects.create(group='ІТ-31', day='tuesday', subjects=['Математика', 'Алгоритмізація'])
    
    def test_unique_together(self):
        with self.assertRaises(IntegrityError):
            Schedule.objects.create(group='ІТ-31', day='tuesday', subjects=['Алгоритмізація'])
            
    def test_get_schedule(self):
        response = self.client.get(reverse('schedule-list'), None, **{'HTTP_AUTHORIZATION': f'ApiKey {settings.API_KEY}'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_group_schedule(self):
        response = self.client.get(reverse('schedule-group', kwargs={'group': 'ІТ-31'}), None, **{'HTTP_AUTHORIZATION': f'ApiKey {settings.API_KEY}'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    