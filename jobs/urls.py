from django.urls import path
from .views import JobList , JobDetail , CategoryList


urlpatterns = [
    path('', JobList.as_view()),
    path('<slug:slug>/', JobDetail.as_view()),
    path('category/', CategoryList.as_view(), name='category-list'),
]