from django.urls import path
from .views import JobList, JobDetail, JobCreate, JobUpdate, JobDelete, JobDeleteConfirm, CategoryList
from .api import   JobListAPI , JobDetailAPI , CompanyListAPI , CompanyDetailAPI


urlpatterns = [
    path('', JobList.as_view(), name='job_list'),
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('add/', JobCreate.as_view(), name='add_job'),
    path('<slug:slug>/', JobDetail.as_view(), name='job_detail'),
    path('<slug:slug>/edit/', JobUpdate.as_view(), name='edit_job'),
    path('<slug:slug>/delete/', JobDelete.as_view(), name='delete_job'),
    path('<slug:slug>/delete/confirm/', JobDeleteConfirm.as_view(), name='delete_job_confirm'),
    

    path('api/list' , JobListAPI.as_view()),
    path('api/list/<int:pk>' , JobDetailAPI.as_view()),
    path('api/list/company' , CompanyListAPI.as_view()),
    path('api/list/company/<int:pk>' , CompanyDetailAPI.as_view()),
]
