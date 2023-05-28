from django.urls import path, include
from rest_framework import routers
from .views import ScheduleViewSet


router = routers.SimpleRouter()
router.register(r'schedule', ScheduleViewSet, 'schedule')

urlpatterns = router.urls
