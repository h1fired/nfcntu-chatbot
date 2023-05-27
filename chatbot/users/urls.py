from django.urls import path, include
from rest_framework import routers
from .views import UserProfileViewSet


router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, 'users')

urlpatterns = router.urls
