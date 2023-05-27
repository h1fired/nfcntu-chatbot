from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Contact
from .permissions import APIKeyPermission


class ContactViewSet(viewsets.ViewSet):
    permission_classes = [APIKeyPermission]
    
    def list(self, request):
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
    
