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
