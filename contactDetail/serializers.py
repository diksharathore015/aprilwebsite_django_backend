from rest_framework import serializers
from .models import ContactDetail

class ContactDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactDetail
        fields = ['id', 'contact_type', 'value', 'label', 'created_at']
        read_only_fields = ['id', 'created_at']
