from rest_framework.routers import DefaultRouter
from .views import ContactDetailViewSet

router = DefaultRouter()
router.register(r'contact-details', ContactDetailViewSet, basename='contactdetail')

urlpatterns = router.urls
