from django.shortcuts import render
from django.http import HttpResponseNotFound
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import UserProfile
from .serializers import UserProfileSerializator
from rest_framework import status

@api_view(['GET'])
def users_list(request):
    users = UserProfile.objects.all()
    serialized_users = UserProfileSerializator(users, many=True)
    return Response(serialized_users.data)

@api_view(['GET'])
def user_detail(request, social_id):
    user = UserProfile.objects.get(social_id=social_id)
    serialized_user = UserProfileSerializator(user, many=False)
    return Response(serialized_user.data)

@api_view(['POST'])
def user_create_or_get(request):
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

@api_view(['POST'])
def user_update(request, social_id):
    if UserProfile.objects.filter(social_id=social_id).exists() is not True:
        return HttpResponseNotFound()
        
    user = UserProfile.objects.get(social_id=social_id)
    serializer = UserProfileSerializator(instance=user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
