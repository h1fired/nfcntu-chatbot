from django.test import TestCase
from .models import UserProfile

# Create your tests here.
class UserProfileTests(TestCase):
    def test_user_creation(self):
        self.user = UserProfile.objects.create(
            social_id='12345678',
            username='test_user1', 
            specialty='Computer Science', 
            group='IT-41', 
            course_num=4
        )
        self.user.username = 'test_updated_user1'
        self.user.save()
