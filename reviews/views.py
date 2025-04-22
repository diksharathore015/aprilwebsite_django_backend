 
from rest_framework import viewsets
from .models import Course
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Review, Course, Student
from .serializers import ReviewSerializer
from django_filters import rest_framework as filters
class ReviewFilter(filters.FilterSet):
    course_title = filters.CharFilter(field_name="course__title", lookup_expr='iexact')
    course_id = filters.CharFilter(field_name="course__id", lookup_expr='iexact')
    class Meta:
        model = Review
        fields = ['course_title' ,'course_id']

from rest_framework.viewsets import ModelViewSet
class ReviewViewSets(ModelViewSet):

    queryset = Review.objects.all()
    course_ids = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        source='courses',
        many=True,
        write_only=True
    )
    students_ids = serializers.PrimaryKeyRelatedField(
        queryset = Student.objects.all() ,
        source = 'student' ,
        many = True ,
        write_only = True ,
    )
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ReviewFilter   
    serializer_class = ReviewSerializer
    class Meta:
        models = Review
        fields =['id']
 
# class ReviewViewSets(viewsets.ModelViewSet):
#     queryset = Review.objects.all()
#     course_ids = serializers.PrimaryKeyRelatedField(
#         queryset=Course.objects.all(),
#         source='courses',
#         many=True,
#         write_only=True
#     )
#     students_ids = serializers.PrimaryKeyRelatedField(
#         queryset = Student.objects.all() ,
#         source = 'student' ,
#         many = True ,
#         write_only = True ,
#     )
#     # filter_backends =Review_Filter
#     serializer_class = ReviewSerializer
#     class Meta:
#         models = Review
#         fields =['id']
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     filterset_class = ReviewFilter  # Use the custom filter class
#     search_fields = ['title', 'content']  # Allow searching by review title or content
#     ordering_fields = ['created_at', 'rating']  # Allow ordering by creation date and rating
#     serializer_class = ReviewSerializer
