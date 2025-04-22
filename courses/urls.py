from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Create a router and register the ViewSets
router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'courses_title', CourseTitleViewSet, basename='courses_title')
router.register(r'instructors', InstructorViewSet)

# router.register(r'courses_homepage', CourseTitleViewSet, basename='courses_homepage')

 

urlpatterns = [
    # Include the router URLs
    path('', include(router.urls)),
]

