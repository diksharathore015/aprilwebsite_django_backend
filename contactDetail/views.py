from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import ContactDetail
from .serializers import ContactDetailSerializer
from .filters import ContactDetailFilter
from django_filters.rest_framework import DjangoFilterBackend

class ContactDetailViewSet(ModelViewSet):
    """
    A viewset for managing ContactDetail objects.
    Provides `list`, `create`, `retrieve`, `update`, and `delete` actions.
    """
    queryset = ContactDetail.objects.all()
    serializer_class = ContactDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ContactDetailFilter
