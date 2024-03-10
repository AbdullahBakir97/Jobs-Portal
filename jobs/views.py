from django.shortcuts import render , redirect
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from .models import Job, Category, Company
from .forms import JobForm, CategoryForm, CompanyForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




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
        if form.is_valid():
            print("Form is valid. Saving data...")
        else:
            print("Form is invalid. Errors:", form.errors)
        return super().form_valid(form)
  


class JobUpdate(UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/edit_job.html'
    success_url = '/jobs/'


class JobDelete(DeleteView):
    model = Job
    template_name = 'jobs/delete.html'
    success_url = reverse_lazy('delete_confirm')

    def get_object(self, queryset=None):
        return get_object_or_404(Job, slug=self.kwargs['job_slug'])

class JobDeleteConfirm(DeleteView):
    model = Job
    template_name = 'jobs/delete_confirm.html'
    success_url = reverse_lazy('job_list')

    def get_object(self, queryset=None):
        return get_object_or_404(Job, slug=self.kwargs['job_slug'])

    def delete(self, request, *args, **kwargs):
        job = self.get_object()
        job.delete()
        return HttpResponseRedirect(self.success_url)



# Category Views

class CategoryList(generic.ListView):
    model = Category
    template_name = 'jobs/category_list.html'

class CategoryDetail(generic.DetailView):
    model = Category
    template_name = 'jobs/category_detail.html'

class CategoryCreate(generic.CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'jobs/add_category.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'jobs/edit_category.html'
    success_url = reverse_lazy('category_list')

class CategoryDelete(DeleteView):
    model = Category
    template_name = 'jobs/delete_category.html'
    success_url = reverse_lazy('category_list')

    def get_object(self, queryset=None):
        return get_object_or_404(Category, slug=self.kwargs['slug'])

# Company Views

class CompanyList(generic.ListView):
    model = Company
    template_name = 'jobs/company_list.html'

class CompanyDetail(generic.DetailView):
    model = Company
    template_name = 'jobs/company_detail.html'

class CompanyCreate(generic.CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'jobs/add_company.html'
    success_url = reverse_lazy('company_list')

class CompanyUpdate(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'jobs/edit_company.html'
    success_url = reverse_lazy('company_list')

class CompanyDelete(DeleteView):
    model = Company
    template_name = 'jobs/delete_company.html'
    success_url = reverse_lazy('company_list')

    def get_object(self, queryset=None):
        return get_object_or_404(Company, slug=self.kwargs['slug'])
    
    