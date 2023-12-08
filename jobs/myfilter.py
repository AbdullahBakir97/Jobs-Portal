from django_filters import rest_framework as filters
from .models import Job



class JobFilter(filters.FilterSet):
    class Meta:
        model = Job
        fields = {
            'title': ['contains', ],
            'salary': ['lte', 'gte', 'range'],
            'job_nature': ['exact'],
            'agency': ['exact'],
            'vacancy': ['exact'],
            
        }