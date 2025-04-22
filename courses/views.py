 
from rest_framework import viewsets
from .models import Course
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CourseFilter  # Optional: if you have custom filtering

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('-created_at')  # You can filter the courses based on your needs
    serializer_class = CourseSerializer  # Use the CourseSerializer created above
    http_method_names = ['get', 'post', 'patch', 'delete']  # Allow the common HTTP methods
    filter_backends = [DjangoFilterBackend]  # Optional, if you have filtering setup
    filterset_class = CourseFilter  # Optional, if you have a custom filter
    ordering = ['-created_at']  # Optional: Order courses by creation date (latest first)
class CourseTitleViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class =  CourseTitleSerializer 
    class Meta:
        model= Course
        fields = ['id','title' ,'short_description']

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']
    serializer_class = InstructorSerializer

