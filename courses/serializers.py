from rest_framework import serializers
from location.models import State, City, Locality
from .models import Course
from location.serializers import *
from allstudents.serializers import *

from allstudents.models import Student

class CourseSerializer(serializers.ModelSerializer):
    # Use nested serializers for related models
    state = StatesNestedSerializer(many=True, read_only=True)
    city = CityNestedSerializer(many=True, read_only=True)
    locality = LocalitiesNestedSerializer(many=True, read_only=True)
    student_list = StudentSerializer(many=True, read_only=True)
    state_ids = serializers.PrimaryKeyRelatedField(
        queryset=State.objects.all(),
        source='state',
        many=True,
        write_only=True
    )
    city_ids = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(),
        source='city',
        many=True,
        write_only=True
    )
    localities_ids = serializers.PrimaryKeyRelatedField(
        queryset=Locality.objects.all() ,
        source='locality',
        many=True,
        write_only=True
    )
    student_ids = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all() ,
        source='student_list',
        many=True,
        write_only=True
    )
    class Meta:
        model = Course
        fields = [
            'id', 'title','created_by' ,  'price' ,'duration','short_description', 'description', 'slider_images', 
            'meta_title', 'meta_description', 'meta_keywords', 'contact_number', 
            'youtube_link', 'facebook_link', 'instagram_link', 'created_at', 
            'updated_at', 'slug', 'state', 'city', 'locality' ,'state_ids' , 'city_ids' ,'localities_ids'  ,'student_list' ,'student_ids'
        ]
def validate_title(self, value):
        if Course.objects.filter(title=value).exists():
            raise serializers.ValidationError("A course with this title already exists.")
        return value
def update(self, instance, validated_data):
    # Update student_list even if it's an empty list
    student_list = validated_data.pop('student_list', None)
    if student_list is not None:
        instance.student_list.set(student_list)

    state = validated_data.pop('state', None)
    if state is not None:
        instance.state.set(state)

    city = validated_data.pop('city', None)
    if city is not None:
        instance.city.set(city)

    locality = validated_data.pop('locality', None)
    if locality is not None:
        instance.locality.set(locality)

    return super().update(instance, validated_data)

    

class CourseTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','title' ,'slug'] 

class InstructorSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Course.objects.all()
    )  # Reference Course by IDs

    class Meta:
        model = Instructor
        fields = '__all__'