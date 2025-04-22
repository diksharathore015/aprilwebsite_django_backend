from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register(r'media', MediaViewSet, basename='media')
router.register(r'videos', MediaVideoViewSet, basename='video')
 
urlpatterns = [
    path('', include(router.urls)), 
]
