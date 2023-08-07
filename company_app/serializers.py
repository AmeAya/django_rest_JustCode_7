from rest_framework.serializers import ModelSerializer
from .models import *


class CompanySerializer(ModelSerializer):
    # Serializer - инструмент, которые конвертирует обычный query в json
    class Meta:
        model = Company
        fields = '__all__'

    # to_representation - Это и есть обработчик в JSON
    # instance - Объект модели, которая приходит в сериалайзер
    # Функция должна вернуть словарь
    def to_representation(self, instance):
        representation = dict()
        representation['id'] = instance.id
        representation['name'] = instance.name
        representation['bin'] = int(instance.bin)
        representation['country'] = instance.country
        representation['employee_count'] = instance.employee_count
        representation['industry'] = instance.industry.name
        if instance.parent:
            representation['parent'] = instance.parent.name
        return representation

    # Второй вариант. Использование родительского to_representation()

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['industry'] = instance.industry.name
    #     if representation['parent']:
    #         representation['parent'] = instance.parent.name
    #     else:
    #         del representation['parent']
    #     return representation
