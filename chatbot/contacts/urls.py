from django.urls import path, include
from rest_framework import routers
from .views import ContactViewSet


router = routers.SimpleRouter()
router.register(r'contacts', ContactViewSet, 'contacts')

urlpatterns = router.urls
