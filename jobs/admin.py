from django.contrib import admin
from .models import Job, Category, Company

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'agency', 'location', 'created_at', 'vacancy', 'job_nature')
    list_filter = ('category', 'agency', 'job_nature', 'created_at')
    search_fields = ('title', 'location', 'description', 'knowledge_requirements', 'education_experience')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_count')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'website')
    search_fields = ('name', 'presentation')
    prepopulated_fields = {'slug': ('name',)}

admin.site.site_header = "Your Company Admin"
admin.site.site_title = "Your Company Admin Portal"
admin.site.index_title = "Welcome to Your Company Admin Portal"
