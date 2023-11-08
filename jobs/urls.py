from django.urls import path
from .views import JobList , JobDetail


urlpatterns = [
    path('', JobList.as_view()),
    path('<slug:slug>/', JobDetail.as_view()),
]