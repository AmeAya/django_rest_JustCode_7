from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('companies', TemplateView.as_view(template_name='companies_page.html'), name='companies_url'),
    path('company_detail/<int:company_id>', TemplateView.as_view(template_name='company_detail_page.html'), name='company_detail_url'),

    path('api/companies', CompaniesApiView.as_view(), name='companies_api_url'),
    path('api/company_detail', CompaniesDetailApiView.as_view(), name='company_detail_api_url'),
]
