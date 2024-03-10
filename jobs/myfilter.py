import django_filters
from django_filters import rest_framework as filters
from .models import Job, Category, Company

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    salary__lte = django_filters.NumberFilter(field_name='salary', lookup_expr='lte')
    salary__gte = django_filters.NumberFilter(field_name='salary', lookup_expr='gte')
    job_nature = django_filters.ChoiceFilter(field_name='job_nature')
    agency = django_filters.CharFilter(field_name='agency__name', lookup_expr='icontains')
    vacancy = django_filters.NumberFilter(field_name='vacancy', lookup_expr='exact')

    class Meta:
        model = Job
        fields = []

class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    job_count__lte = django_filters.NumberFilter(field_name='job_count', lookup_expr='lte')
    job_count__gte = django_filters.NumberFilter(field_name='job_count', lookup_expr='gte')

    class Meta:
        model = Category
        fields = []

class CompanyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    email = django_filters.CharFilter(field_name='email', lookup_expr='icontains')

    class Meta:
        model = Company
        fields = []

