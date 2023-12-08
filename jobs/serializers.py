from rest_framework import serializers
from .models import Job , Company , Category
from django.db.models.aggregates import Avg




class JobSerializer(serializers.ModelSerializer):
     class Meta:
        model = Job
        fields = '__all__'



class JobListSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()
    
    class Meta:
        model = Job
        fields = '__all__'



class JobDetailSerializer(serializers.ModelSerializer):
    company= serializers.StringRelatedField()

    class Meta:
        model = Job
        fields = '__all__'



class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        
        
class CompanyDetailSerializer(serializers.ModelSerializer):
    job_company = CompanyListSerializer(many=True)
    class Meta:
        model = Company
        fields = '__all__'