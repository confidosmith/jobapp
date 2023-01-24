from django.contrib import admin
from home.models import *

# Register your models here.

class ConfidoJobinfoAdmin(admin.ModelAdmin):
    list_display= [ 'id', 'name','keyword','logo','favicon','email','website','copyright_year']


admin.site.register(ConfidoJobinfo, ConfidoJobinfoAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']


class ListjobAdmin(admin.ModelAdmin):
    list_display= ['id','employer','category','job_title', 'job_location', 'salary', 'published','closed','featured','tags','deadline','logo','website','posted_at']
    list_editable = ['published', 'closed','featured', 'employer']



admin.site.register(Listjob,ListjobAdmin)
admin.site.register(Category,CategoryAdmin)

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id','listjob','employer', 'employee','first_name','last_name',  'gender','email','cover_letter','resume','applied_at', 'job_location', 'salary']

admin.site.register(Application, ApplicationAdmin)

class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','first_name', 'last_name','gender','email', 'phone']

class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'company', 'phone', 'website', 'email']

admin.site.register(EmployerProfile,EmployerProfileAdmin)
admin.site.register(EmployeeProfile,EmployeeProfileAdmin)