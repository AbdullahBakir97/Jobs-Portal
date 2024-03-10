from django import forms
from .models import Job, Category, Company
from django.utils.translation import gettext_lazy as _

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        labels = {
            'title': _('Title'),
            'category': _('Category'),
            'agency': _('Company'),
            'location': _('Location'),
            'salary': _('Salary'),
            'vacancy': _('Vacancy'),
            'job_nature': _('Job Nature'),
            'application_date': _('Application Date'),
            'description': _('Description'),
            'knowledge_requirements': _('Knowledge & Requirements'),
            'education_experience': _('Education & Experience'),
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'agency': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'vacancy': forms.NumberInput(attrs={'class': 'form-control'}),
            'job_nature': forms.Select(attrs={'class': 'form-control'}),
            'application_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'knowledge_requirements': forms.Textarea(attrs={'class': 'form-control'}),
            'education_experience': forms.Textarea(attrs={'class': 'form-control'}),
        }
        def clean(self):
            cleaned_data = super().clean()
            salary = cleaned_data.get('salary')
            if salary is not None and salary < 0:
                raise forms.ValidationError("Salary cannot be negative.")
            return cleaned_data
        

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name': _('Name'),
            'image': _('Image'),
            'job_count': _('Job Count'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'job_count': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        def clean(self):
            cleaned_data = super().clean()
            job_count = cleaned_data.get('job_count')
            if job_count is not None and job_count < 0:
                raise forms.ValidationError("Job count cannot be negative.")
            return cleaned_data

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        labels = {
            'name': _('Name'),
            'logo': _('Logo'),
            'presentation': _('Presentation'),
            'website': _('Website'),
            'email': _('Email'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'presentation': forms.Textarea(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        def clean(self):
            cleaned_data = super().clean()
            email = cleaned_data.get('email')
            if email is not None and not email.endswith('@example.com'):
                raise forms.ValidationError("Please enter a valid example.com email address.")
            return cleaned_data
