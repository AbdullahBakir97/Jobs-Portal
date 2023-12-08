from rest_framework import generics , filters
from rest_framework.response import Response
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.permissions import IsAuthenticated
from .serializers import JobSerializer , JobListSerializer , JobDetailSerializer , CompanyListSerializer , CompanyDetailSerializer
from .models import Job , Company , Category
from .myfilter import JobFilter
from .mypagination import MyPagination


class JobListAPI(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobListSerializer
    filter_backends = [DjangoFilterBackend , filters.SearchFilter , filters.OrderingFilter]
    filterset_fields = ['job_nature', 'agency']
    search_fields = ['title', 'category', 'location']
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


class JobCreateDetailDeleteAPI(generics.GenericAPIView):
    serializer_class = JobSerializer

    def get(self,request):
        
        job , created = Job.objects.get_or_create()
        data = JobSerializer(job).data
        return Response({'job':data})
    
    def post(self,request):

        job = Job.objects.get(id=request.data['job_id'])
        vacancy = int(request.data['vacancy'])

        job_detail,created = JobDetailAPI.objects.get_or_create(job=job)
        return Response({'massege':'job was addedd successufly'})

    def delete(self,request,*args, **kwargs):

 
        job = JobDetailAPI.objects.get(id=request.data['job_id'])
        job.delete()
        return Response({'massage':'job was deleted successfuly'})