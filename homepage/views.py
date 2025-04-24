from django.shortcuts import render
 
 

from rest_framework import viewsets
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import FAQFilter
class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banners.objects.all() 
    serializer_class = BannerSerializer
class SeoViewSet(viewsets.ModelViewSet):
    queryset = SEO.objects.all()
    serializer_class = SeoSerializer
    
class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FAQFilter
    http_method_names = ['get', 'post', 'delete','patch']

class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
class home_page_dataViewSet(viewsets.ModelViewSet):
    queryset = home_page_data.objects.all()
    serializer_class = home_page_dataSerializer
    
class EnquieryFormViewSet(viewsets.ModelViewSet):
    queryset = EnquiryForm.objects.all()
    serializer_class= EnquieryFormSerializer
    http_method_names = ['get', 'post', 'delete','patch']
