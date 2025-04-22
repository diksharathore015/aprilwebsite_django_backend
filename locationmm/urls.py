from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StateViewSet, CityViewSet, LocalityViewSet

# Create a router and register the ViewSets
router = DefaultRouter()
router.register(r'states', StateViewSet, basename='state')
router.register(r'cities', CityViewSet, basename='city')
router.register(r'localities', LocalityViewSet, basename='locality')

urlpatterns = [
    # Include the router URLs
    path('', include(router.urls)),
]

