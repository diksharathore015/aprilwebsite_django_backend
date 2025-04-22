from rest_framework import serializers
from location.models import State, City, Locality
from .models import Course
from location.serializers import *
from courses.serializers import *
from allstudents.serializers import *
from .models import *
class ReviewSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=True ,read_only= True)
    student = StudentSerializer(many=True  , read_only= True)
    course_ids = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        source='course',
        many=True,
        write_only=True
    )
    students_ids = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(),
        source='student',
        many=True,
        write_only=True
    )
  
    class Meta:
        model = Review
        fields =[ "id",
    "title",
    "content",
    "rating",
    "created_at" ,
    "student" ,"students_ids",
    "course" ,"course_ids" ]


