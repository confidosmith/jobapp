from django.contrib import admin

from userprofile.models import *

# Register your models here.
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','first_name', 'last_name','gender','email']

class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'company', 'phone', 'website', 'email']

admin.site.register(EmployerProfile,EmployerProfileAdmin)
admin.site.register(EmployeeProfile,EmployeeProfileAdmin)
