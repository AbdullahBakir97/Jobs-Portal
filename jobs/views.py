from django.shortcuts import render
from django.views import generic
from .models import Job , Category , Company

class JobList(generic.ListView):
    model = Job


class JobDetail(generic.DetailView):
    model = Job


class CategoryList(generic.ListView):
    model = Category