from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']


class ListjobAdmin(admin.ModelAdmin):
    list_display= ['id','employer','category','job_title', 'job_location', 'salary', 'published','closed','featured','tags','deadline','logo','website','posted_at']
    list_editable = ['published', 'closed','featured', 'employer']



admin.site.register(Listjob,ListjobAdmin)
admin.site.register(Category,CategoryAdmin)