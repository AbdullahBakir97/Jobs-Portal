from django.shortcuts import render , redirect
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import UpdateView
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


class JobUpdate(UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/edit_job.html'
    success_url = '/jobs/'


class JobDelete(generic.DeleteView):
    model = Job
    template_name = 'jobs/delete_job.html'
    success_url = reverse_lazy('job_list')

    #def get(self, request, *args, **kwargs):
        # Display the initial delete page
        #return render(request, self.template_name, {'job': self.get_object()})

class JobDeleteConfirm(generic.DeleteView):
    model = Job
    template_name = 'jobs/delete_job_confirm.html'
    success_url = reverse_lazy('job_list')

    def post(self, request, *args, **kwargs):
        # Handle the actual deletion on a POST request
        job = self.get_object()
        job.delete()
        return render(request, self.template_name, {'job': job})



class CategoryList(generic.ListView):
    model = Category
    template_name = 'jobs/category_list.html'