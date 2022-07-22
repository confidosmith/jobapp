from django.contrib import admin
from . models import * 

# Register your models here.
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id','listjob','employer', 'employee','first_name','last_name',  'gender','email','cover_letter','resume','applied_at', 'job_location', 'salary']

admin.site.register(Application, ApplicationAdmin)