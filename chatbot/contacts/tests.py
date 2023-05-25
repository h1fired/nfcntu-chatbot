from rest_framework.test import APITestCase
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from .models import Contact
from django.conf import settings

class ContactAPITest(APITestCase):
    
    def setUp(self):
        Contact.objects.create(name='test_contacts1', contact='test_contacts1', group='test_administration1')
        
    def test_get_contacts(self):
        response = self.client.get(reverse('contacts-list'), None, **{'HTTP_AUTHORIZATION': f'ApiKey {settings.API_KEY}'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)