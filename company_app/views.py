from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


class CompaniesApiView(APIView):
    permission_classes = []

    def get(self, request):
        companies = Company.objects.all()
        # Данные нужно превратить в JSON - сериализация
        data = {
            'companies': CompanySerializer(companies, many=True).data
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Company created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Server Error'}, status=status.HTTP_400_BAD_REQUEST)



class CompaniesDetailApiView(APIView):
    permission_classes = []

    def get(self, request):
        company_id = request.GET.get('company_id')
        # Достаем из отправленных параметров ключ company_id
        company = get_object_or_404(Company, id=company_id)
        data = {
            'company': CompanySerializer(company).data
        }
        return Response(data, status=status.HTTP_200_OK)

    def delete(self, request):
        company_id = request.data['company_id']
        company = Company.objects.filter(pk=company_id)  # filter - Возвращает лист объектов
        # Так как мы ищем по pk, то максимум мы найдем 1 запись
        # pk(id) уникальны!
        if company:  # if срабатывает тогда, когда лист не пустой
            company[0].delete()
            return Response({'message': 'Company is deleted'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Company not found'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        company_id = request.data['company_id']
        company = Company.objects.filter(pk=company_id)
        if company:
            serializer = CompanySerializer(company[0], data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Company is updated'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Wrong keys!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Company not found'}, status=status.HTTP_400_BAD_REQUEST)


# Создать сериалайзер для Industry.
# Создать два Апи вью для Industry:
#   1) GetAllIndustries -> Возвращает все Индустрии
#   2) GetIndustryDetail -> Возвращает только 1 индустрию по id, который принимает.
# Создать Апи вью, возвращающий только те Индустрии, имена которых начинаются на букву, принятую get запросом
