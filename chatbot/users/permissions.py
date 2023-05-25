from rest_framework.permissions import BasePermission
from django.conf import settings

class APIKeyPermission(BasePermission):
    def has_permission(self, request, view):
        try:
            meta_api_key = request.META['HTTP_AUTHORIZATION']
            if meta_api_key != f'ApiKey {settings.API_KEY}':
                return False
            return True
        except:
            return False
        
        