from rest_framework.test import APITestCase
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from .models import Announcement
from django.conf import settings

class AnnouncementAPITest(APITestCase):
    
    def setUp(self):
        Announcement.objects.create(title='test_title1', description='test_desc1')
        
    def test_get_announecements(self):
        response = self.client.get(reverse('announcement-list'), None, **{'HTTP_AUTHORIZATION': f'ApiKey {settings.API_KEY}'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)