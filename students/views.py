from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
 
# Create your views here.
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Students
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'states__id': ['exact'],       # Filter by State ID
        'cities__id': ['exact'],       # Filter by City ID
        'localities__id': ['exact'],   # Filter by Locality ID
        'courses__id': ['exact'],      # Filter by Course ID
    }
    search_fields = ['name']           # Enable search by name
    ordering_fields = ['name']        # Enable ordering by name