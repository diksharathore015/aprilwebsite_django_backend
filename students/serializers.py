from rest_framework import serializers
from .models import *
from courses.models import *
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from media.serializers import *
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','title']

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'state_name']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city_name']

class LocalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Locality
        fields = ['id', 'locality_name']
class StudentSerializer(serializers.ModelSerializer):
    course_ids = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        source='courses',
        many=True,
        write_only=True
    )
  
    state_ids = serializers.PrimaryKeyRelatedField(
        queryset=State.objects.all(),
        source='states',
        many=True,
        write_only=True
    )
    city_ids = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(),
        source='cities',
        many=True,
        write_only=True
    )
    localities_ids = serializers.PrimaryKeyRelatedField(
        queryset=Locality.objects.all(),
        source='localities',
        many=True,
        write_only=True
    )
    courses = CourseSerializer(many=True, read_only=True)
    states = StateSerializer(many=True, read_only=True)
    cities = CitySerializer(many=True, read_only=True)
    localities = LocalitySerializer(many=True, read_only=True)
    image = MediaSerializer(many=True, read_only=True)
    class Meta:
        model = Students
        fields = [
            'id', 'name', 'image' , 'courses', 'course_ids', 'states', 'state_ids' ,'cities', 'city_ids', 'localities', 'localities_ids','detail', 'contact_number' ,'youtube_link' ,'facebook_link' ,'instagram_link',
            'meta_title', 'meta_descriptions', 'meta_keyWords' , 'rating' ,'review' ,  
        ]

 