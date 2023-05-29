from rest_framework.test import APITestCase
from rest_framework import status
from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse
from .models import UserProfile, Group, Specialty
from django.conf import settings


class UserProfileTests(TestCase):
    def test_user_creation(self):
        self.user = UserProfile.objects.create(
            social_id='12345678',
            username='test_user1', 
        )
        self.user.username = 'test_updated_user1'
        self.user.save()

class UserProfileAPITest(APITestCase):
    def setUp(self):
        UserProfile.objects.create(social_id='12345678', username='test_user123')
    
    def test_get_users(self):
        response = self.client.get(reverse('users-list'), None, **{'HTTP_AUTHORIZATION': f'ApiKey {settings.API_KEY}'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_user(self):
        response = self.client.get(reverse('users-detail', kwargs={'social_id': 12345678}), None, **{'HTTP_AUTHORIZATION': f'ApiKey {settings.API_KEY}'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_or_get_user(self):
        data = {
            'social_id': '12345',
            'username': 'test_create_user1'
        }
        response = self.client.post(reverse('users-list'), data, format='json', **{'HTTP_AUTHORIZATION': f'ApiKey {settings.API_KEY}'})
        self.assertNotEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_update_user(self):
        data = {
            'username': 'test_update_user6'
        }
        response = self.client.patch(reverse('users-detail', kwargs={'social_id': 12345678}), data, format='json', **{'HTTP_AUTHORIZATION': f'ApiKey {settings.API_KEY}'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

class GroupAPITest(APITestCase):
    def setUp(self):
        specialty = Specialty.objects.create(name='test_specialty')
        Group.objects.create(name='test_group1', specialty=specialty)
        
    def test_unique(self):
        with self.assertRaises(IntegrityError):
            specialty = Specialty.objects.get(name='test_specialty')
            Group.objects.create(name='test_group1', specialty=specialty)
            
    def test_get_list(self):
        response = self.client.get(reverse('groups-list'), None, **{'HTTP_AUTHORIZATION': f'ApiKey {settings.API_KEY}'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class SpecialtyAPITest(APITestCase):
    def setUp(self):
        Specialty.objects.create(name='test_specialty')
        
    def test_unique(self):
        with self.assertRaises(IntegrityError):
            Specialty.objects.create(name='test_specialty')
            
    def test_get_list(self):
        response = self.client.get(reverse('specialty-list'), None, **{'HTTP_AUTHORIZATION': f'ApiKey {settings.API_KEY}'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)