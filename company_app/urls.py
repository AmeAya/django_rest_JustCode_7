from django.urls import path
from .views import *

urlpatterns = [
    path('all_companies', CompaniesApiView.as_view(), name='all_companies_url'),
    path('company_detail', CompaniesDetailApiView.as_view(), name='company_detail_url'),
]
