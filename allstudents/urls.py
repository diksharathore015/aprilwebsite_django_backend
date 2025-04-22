from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  *

# Create a router and register the ViewSets
router = DefaultRouter()
router.register(r'allstudentslist',  StudentViewSet, basename='students')
# router.register(r'allstudentslist',  StudentViewSet, basename='students')

router.register(r'studentslist', StudentlistViewSet , basename = "studentlist")
urlpatterns = [
    # Include the router URLs
    path('', include(router.urls)),
]

