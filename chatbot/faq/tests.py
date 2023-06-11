from rest_framework.test import APITestCase
from rest_framework import status
from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse
from users.models import UserProfile
from .models import FAQ
from django.conf import settings


class FAQTests(TestCase):
    def setUp(self):
        self.user = UserProfile.objects.create(social_id='12345678', chat_id='87654321', username='test_user123')
    
    def test_faq_creation(self):
        FAQ.objects.create(
            user=self.user,
            question='Test Question'
        )

class FAQAPITest(APITestCase):
    def setUp(self):
        UserProfile.objects.create(social_id='12345678', chat_id='87654321', username='test_user123')
    
    def test_create_faq(self):
        data = {
            'user': 12345678,
            'question': 'Test Question'
        }
        
        response = self.client.post(reverse('faq-list'), data, format='json', **{'HTTP_AUTHORIZATION': f'ApiKey {settings.API_KEY}'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)