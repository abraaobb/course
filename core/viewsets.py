from rest_framework import viewsets
from core import models, serializers


class CouseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
