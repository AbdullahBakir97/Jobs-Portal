from django.urls import path
from .views import (JobList, JobDetail, JobCreate, JobUpdate, JobDelete, JobDeleteConfirm, 
                    CategoryList, CategoryDetail, CategoryCreate, CategoryUpdate, CategoryDelete, 
                    CompanyList, CompanyDetail, CompanyCreate, CompanyUpdate, CompanyDelete)
from .api import   JobListAPI , JobDetailAPI , CompanyListAPI , CompanyDetailAPI


urlpatterns = [
    path('', JobList.as_view(), name='job_list'),
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('add/', JobCreate.as_view(), name='add_job'),
    path('<slug:slug>/', JobDetail.as_view(), name='job_detail'),
    path('<slug:slug>/edit/', JobUpdate.as_view(), name='edit_job'),
    path('<slug:job_slug>/delete/', JobDelete.as_view(), name='delete_job'),
    path('<slug:job_slug>/delete/confirm/', JobDeleteConfirm.as_view(), name='delete_job_confirm'),
    
    # Category URLs
    path('categories/',CategoryList.as_view(), name='category_list'),
    path('categories/add/',CategoryCreate.as_view(), name='category_add'),
    path('categories/<slug:slug>/',CategoryDetail.as_view(), name='category_detail'),
    path('categories/<slug:slug>/edit/',CategoryUpdate.as_view(), name='category_edit'),
    path('categories/<slug:slug>/delete/',CategoryDelete.as_view(), name='category_delete'),

    # Company URLs
    path('companies/',CompanyList.as_view(), name='company_list'),
    path('companies/add/',CompanyCreate.as_view(), name='company_add'),
    path('companies/<slug:slug>/',CompanyDetail.as_view(), name='company_detail'),
    path('companies/<slug:slug>/edit/',CompanyUpdate.as_view(), name='company_edit'),
    path('companies/<slug:slug>/delete/',CompanyDelete.as_view(), name='company_delete'),
    

    path('api/list' , JobListAPI.as_view()),
    path('api/list/<int:pk>' , JobDetailAPI.as_view()),
    path('api/list/company' , CompanyListAPI.as_view()),
    path('api/list/company/<int:pk>' , CompanyDetailAPI.as_view()),
]
