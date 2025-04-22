import django_filters 
from .models import *

class StateFilter(django_filters.FilterSet):
    state_name = django_filters.CharFilter(lookup_expr='contains')
    class Meta:
        model = State
        fields = ['state_name',]
class CityFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = City
        fields = ['state','city_name']
class LocalityFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='contains')
    locality_name= django_filters.CharFilter(lookup_expr='contains')
    class Meta:
        model = Locality
        fields = ['city','locality_name']