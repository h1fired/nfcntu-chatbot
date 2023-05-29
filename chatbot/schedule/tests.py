from rest_framework.test import APITestCase
from rest_framework import status
from django.db import IntegrityError
from django.urls import reverse
from .models import Schedule
from users.models import Group, Specialty
from django.conf import settings

# Unique Together test
class UserProfileAPITest(APITestCase):
    
    def setUp(self):
        specialty = Specialty.objects.create(name='test_specialty')
        group = Group.objects.create(name='test_group', specialty=specialty)
        Schedule.objects.create(group=group, day='tuesday', subjects=['Математика', 'Алгоритмізація'])
    
    def test_unique_together(self):
        with self.assertRaises(IntegrityError):
            group = Group.objects.get(name='test_group')
            Schedule.objects.create(group=group, day='tuesday', subjects=['Алгоритмізація'])
            
    def test_get_schedule(self):
        response = self.client.get(reverse('schedule-list'), None, **{'HTTP_AUTHORIZATION': f'ApiKey {settings.API_KEY}'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_group_schedule(self):
        response = self.client.get('%s?group=test_group' % reverse('schedule-list'), None, **{'HTTP_AUTHORIZATION': f'ApiKey {settings.API_KEY}'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    