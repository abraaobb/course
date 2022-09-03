from rest_framework.routers import DefaultRouter
from core import viewsets

router = DefaultRouter()
router.register('course', viewsets.CourseViewSet)

urlpatterns = router.urls
