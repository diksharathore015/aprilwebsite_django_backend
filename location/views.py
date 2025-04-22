from rest_framework.viewsets import ModelViewSet
from .models import State, City, Locality
from .serializers import *
from .filter import *
from django_filters.rest_framework import DjangoFilterBackend

class StateViewSet(ModelViewSet):
    queryset = State.objects.all()  # Efficient query to get cities
    serializer_class = StateSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_class =  StateFilter


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_class =  CityFilter

    
class LocalityViewSet(ModelViewSet):

    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_class =  LocalityFilter
