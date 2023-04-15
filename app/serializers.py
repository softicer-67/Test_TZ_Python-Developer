from rest_framework import serializers
from app.models import EducationModule


class EducationModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationModule
        fields = '__all__'
