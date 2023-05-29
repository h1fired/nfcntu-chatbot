from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.SimpleRouter()
router.register(r'users', views.UserProfileViewSet, 'users')
router.register(r'specialty', views.SpecGroupViewset, 'specialty')

urlpatterns = router.urls
