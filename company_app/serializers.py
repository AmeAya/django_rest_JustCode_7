from rest_framework.serializers import ModelSerializer
from .models import *


class CompanySerializer(ModelSerializer):
    # Serializer - инструмент, которые конвертирует обычный query в json
    class Meta:
        model = Company
        fields = '__all__'
