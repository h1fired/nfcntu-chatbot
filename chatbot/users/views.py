from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializator
from .permissions import APIKeyPermission

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializator
    http_method_names = ['get', 'post', 'put', 'patch']
    lookup_field = 'social_id'
    permission_classes = [APIKeyPermission]
    
    def create(self, request):
        if UserProfile.objects.filter(social_id=request.data['social_id']).exists():
            user = UserProfile.objects.get(social_id=request.data['social_id'])
            serialized_user = UserProfileSerializator(user, many=False)
            return Response(serialized_user.data)
        serializer = UserProfileSerializator(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
    