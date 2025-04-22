from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from .models import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination
# Create your views here.
from .filter import * 
class mediaPagination(PageNumberPagination):

    page_size = 20  # Default number of items per page
    page_size_query_param = 'limit'  # Allow clients to set custom limit
    max_page_size = 2000  # Upper limit for page size
class mediavideoPagination(PageNumberPagination):
    page_size = 20  # Default number of items per page
    page_size_query_param = 'limit'  # Allow clients to set custom limit
    max_page_size = 2000  # Upper limit for page size
class MediaViewSet(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class =MediaSerializer
    pagination_class = mediaPagination
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_class =  MediaFilter
    total_size = queryset.aggregate(total_size=models.Sum('size'))['total_size'] or 0
    http_method_names = ['get' , 'post' , 'patch' , 'delete']

class MediaVideoViewSet(ModelViewSet):
    queryset = Media_video.objects.all()
    serializer_class =MediaVideoSerializer
    pagination_class = mediavideoPagination
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_class =  MediavideoFilter
    total_size = queryset.aggregate(total_size=models.Sum('size'))['total_size'] or 0
    http_method_names = ['get' , 'post' , 'patch' , 'delete']
