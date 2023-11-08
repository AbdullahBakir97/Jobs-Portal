from django.contrib import admin
from .models import Job , Category , Company

class JobAdmin(admin.ModelAdmin):
    list_display=['title','category','agency','salary','location']
    list_filter=['job_nature','category','agency']
    search_fields=['title','nature','salary','agency']


admin.site.register(Job,JobAdmin)
admin.site.register(Category)
admin.site.register(Company)
