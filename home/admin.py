from django.contrib import admin
from .models import *

# Register your models here.

class ConfidoJobinfoAdmin(admin.ModelAdmin):
    list_display= ['name','keyword','logo','favicon','email','website','copyright_year']


admin.site.register(ConfidoJobinfo, ConfidoJobinfoAdmin)