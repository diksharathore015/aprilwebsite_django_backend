from rest_framework import serializers
from .models import State, City, Locality
class CityNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
class LocalitiesNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locality
        fields = '__all__'
class StatesNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'state_name', 'title', 'image']
class StateSerializer(serializers.ModelSerializer):
    cities = CityNestedSerializer(many=True, read_only=True,  )  # Assuming `city_set` is the related name

    class Meta:
        model = State
        fields = [
            'id', 'state_name', 'title', 'image', 'meta_title', 'meta_description',
            'meta_keywords', 'description', 'short_description',
            'contact_number', 'facebook', 'instagram', 'whatsapp_number',
            'youtube_link', 'cities' , 'lat' , 'long', 'pincode'
        ]
class CitySerializer(serializers.ModelSerializer):
    state =serializers.PrimaryKeyRelatedField(queryset=State.objects.all())  # Nested StateSerializer to get full state details
    localities = LocalitiesNestedSerializer(many=True, read_only=True)
    state_object = StatesNestedSerializer(source='state', read_only=True)
    class Meta:
        model = City
        fields = [
            'id', 'state', 'city_name', 'state_object' , 'title', 'image', 'meta_title', 'meta_description',
            'meta_keywords', 'description', 'short_description',
            'contact_number', 'facebook', 'instagram', 'whatsapp_number',
            'youtube_link', 'localities' , 'lat' , 'long', 'pincode'
        ]
class LocalitySerializer(serializers.ModelSerializer):
    # city = CityNestedSerializer(read_only=True)
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())
    city_object = CityNestedSerializer(source='city', read_only=True) 
    class Meta:
        model = Locality
        fields = [
            'id', 'city', 'locality_name', 'city_object' ,'title', 'image', 'meta_title', 'meta_description',
            'meta_keywords', 'description', 'short_description',
            'contact_number', 'facebook', 'instagram', 'whatsapp_number',
            'youtube_link',  'lat' , 'long', 'pincode'
        ]
