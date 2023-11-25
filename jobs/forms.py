from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'description', 'location', 'salary', 'category', 'agency', 'vacancy', 'job_nature', 'application_date', 'knowledge_requirements', 'education_experience')

    