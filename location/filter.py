import django_filters 
from .models import *
class StateInFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
    pass
class CityInFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
    pass
class StateFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = State
        fields = ['state_name',]
class CityFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    state = StateInFilter(field_name='state__id', lookup_expr='in')
    class Meta:
        model = City
        fields = ['state','title']
class LocalityFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    city = CityInFilter(field_name='city__id', lookup_expr='in')
 
    class Meta:
        model = Locality
        fields = ['city','title',]