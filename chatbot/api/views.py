from django.http import HttpResponseNotFound
from django.db.models import Count
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import UserProfile
from contacts.models import Contact
from .serializers import UserProfileSerializator, ContactSerializator
from rest_framework import status 
from .permissions import APIKeyPermission

@api_view(['GET'])
@permission_classes([APIKeyPermission])
def users_list(request):
    users = UserProfile.objects.all()
    serialized_users = UserProfileSerializator(users, many=True)
    return Response(serialized_users.data)

@api_view(['GET'])
@permission_classes([APIKeyPermission])
def user_detail(request, social_id):
    try:
        user = UserProfile.objects.get(social_id=social_id)
        serialized_user = UserProfileSerializator(user, many=False)
        return Response(serialized_user.data)
    except UserProfile.DoesNotExist:
        return HttpResponseNotFound(f'User with social_id={social_id} not found')

@api_view(['POST'])
@permission_classes([APIKeyPermission])
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
@permission_classes([APIKeyPermission])
def user_update(request, social_id):
    if UserProfile.objects.filter(social_id=social_id).exists() is not True:
        return HttpResponseNotFound(f'User with social_id={social_id} not found')
        
    user = UserProfile.objects.get(social_id=social_id)
    serializer = UserProfileSerializator(instance=user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


# Contacts
@api_view(['GET'])
@permission_classes([APIKeyPermission])
def contact_list(request):
    contacts = list(Contact.objects.all().values())
    contact_dict = {}
    for contact in contacts:
        if contact['group'] not in contact_dict:
            contact_dict[contact['group']] = []
        contact_dict[contact['group']].append({
            'name': contact['name'],
            'contact': contact['contact']
        })
    return Response(contact_dict)
