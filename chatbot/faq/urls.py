from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.SimpleRouter()
router.register(r'faq', views.FAQViewSet, 'faq')

urlpatterns = router.urls
