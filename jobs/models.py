from django.db import models
from collections.abc import Iterable
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

NATURE_TYPES = (('Full Time','Full Time'),('Part Time','Part Time'),('Remote','Remote'),('Freelance','Freelance'),)

class Job(models.Model):
    title = models.CharField(_('Title'),max_length=150)
    category = models.ForeignKey('Category',verbose_name=_('Category'),related_name='job_category',on_delete=models.SET_NULL,null=True,blank=True)
    agency = models.ForeignKey('Company',verbose_name=_('Company'),related_name='job_company',on_delete=models.SET_NULL,null=True,blank=True)
    location = models.CharField(_('Location'),max_length=150)
    salary = models.FloatField(_('Salary'),)
    created_at = models.DateTimeField(_('Created at'),default=timezone.now)
    vacancy = models.IntegerField(_('Vacancy'),)
    job_nature = models.CharField(_('Job Nature'),max_length=20,choices=NATURE_TYPES)
    application_date = models.DateField(_('Application Date'),)
    description = models.TextField(_('Description'),max_length=50000)
    knowledge_requirements = models.TextField(_('Knowledge Requirements'),max_length=10000)
    education_experience = models.TextField(_('Education Experience'),max_length=10000)
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) 
        super(Job, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(_('Name'),max_length=150)
    image = models.ImageField(_('Image'),upload_to='categories')
    job_count = models.IntegerField(_('Job Count'),)
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Company(models.Model):
    name = models.CharField(_('Name'),max_length=150)
    logo = models.ImageField(_('Logo'),upload_to='company')
    presentation = models.TextField(_('Presentation'),max_length=10000)
    website = models.TextField(_('Website'),max_length=300)
    email = models.TextField(_('Email'),max_length=300)
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)   
        super(Company, self).save(*args, **kwargs)


        