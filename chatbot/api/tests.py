from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import UserProfile

from rest_framework import status

class UserProfileAPITest(APITestCase):
    def setUp(self):
        UserProfile.objects.create(social_id='12345678', username='test_user123')
    
    def test_get_users(self):
        response = self.client.get(reverse('api_users_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_user(self):
        response = self.client.get(reverse('api_user', kwargs={'social_id': 12345678}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_or_get_user(self):
        data = {
            'social_id': '12345',
            'username': 'test_create_user1'
        }
        response = self.client.post(reverse('api_user_create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_update_user(self):
        data = {
            'username': 'test_update_user6'
        }
        response = self.client.post(reverse('api_user_update', kwargs={'social_id': 12345678}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
