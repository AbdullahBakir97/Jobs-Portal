from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Job, Category, Company
from .forms import JobForm  

class JobList(generic.ListView):
    model = Job
    template_name = 'jobs/job_list.html'

class JobDetail(generic.DetailView):
    model = Job
    template_name = 'jobs/job_detail.html'

class JobCreate(generic.CreateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/add_job.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JobUpdate(generic.UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/edit_job.html'

class JobDelete(generic.DeleteView):
    model = Job
    success_url = reverse_lazy('job_list')
    template_name = 'jobs/delete_job_confirm.html'


class CategoryList(generic.ListView):
    model = Category
    template_name = 'jobs/category_list.html'