from rest_framework.viewsets import ModelViewSet
from app.models import EducationModule
from app.serializers import EducationModuleSerializer


class EducationModuleViewSet(ModelViewSet):
    queryset = EducationModule.objects.all()
    serializer_class = EducationModuleSerializer
