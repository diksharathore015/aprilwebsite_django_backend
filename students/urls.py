from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  *

# Create a router and register the ViewSets
router = DefaultRouter()
router.register(r'allstudents',  StudentViewSet, basename='students')

urlpatterns = [
    # Include the router URLs
    path('', include(router.urls)),
]

