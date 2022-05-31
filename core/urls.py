from rest_framework.routers import DefaultRouter
from core import viewsets

router = DefaultRouter()
router.register('course', viewsets.CouseViewSet)

urlpatterns = router.urls
