from typing import Any, Optional
from django.core.management.base import BaseCommand
from users.models import UserProfile

class Command(BaseCommand):
    help = 'Creating test users'
    
    def handle(self, *args, **options):
        for index in range(5):
            UserProfile.objects.create(
                social_id=index, 
                username='c_test_user'+str(index), 
                first_name='c_test_fn'+str(index), 
                last_name='c_test_ln'+str(index),
                group='IT-%s1'%str(index),
                specialty='Computer Science',
                course_num=4
            )
            self.stdout.write('TestUser%s created.' % str(index))
        self.stdout.write(self.style.SUCCESS('Test users created.'))
        