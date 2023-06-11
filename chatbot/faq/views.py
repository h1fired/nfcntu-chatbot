from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializator
from users.permissions import APIKeyPermission

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializator
    http_method_names = ['post']
    permission_classes = [APIKeyPermission]