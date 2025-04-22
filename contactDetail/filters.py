from django_filters import rest_framework as filters
from .models import ContactDetail

class ContactDetailFilter(filters.FilterSet):
    contact_type = filters.ChoiceFilter(choices=ContactDetail.TYPE_CHOICES)

    class Meta:
        model = ContactDetail
        fields = ['contact_type']
