from rest_framework import generics, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .serializers import JobSerializer, JobListSerializer, JobDetailSerializer, CompanyListSerializer, CompanyDetailSerializer, CompanySerializer
from .models import Job, Company
from .myfilter import JobFilter
from .mypagination import MyPagination

class JobListAPI(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['job_nature', 'agency']
    search_fields = ['title', 'location'] 
    ordering_fields = ['salary', 'vacancy']
    filterset_class = JobFilter
    pagination_class = MyPagination

class JobDetailAPI(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobDetailSerializer

class CompanyListAPI(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer
    pagination_class = MyPagination

class CompanyDetailAPI(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer

class JobCreateAPI(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        serializer.save()

class JobDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

class CompanyCreateAPI(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def perform_create(self, serializer):
        serializer.save()

class CompanyDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]
