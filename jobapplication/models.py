from django.db import models
from postjob.models import Listjob

from userprofile.models import EmployeeProfile

# Create your models here.

class Application(models.Model):  
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
    listjob = models.CharField(max_length=250, blank=True, null=True)
    employer = models.CharField(max_length=250, blank=True, null=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=50)
    email = models.EmailField()
    job_location = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)
    display = models.BooleanField(null=True, blank=True, default=True)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='resume', default='resume')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee.user.username


    class Meta:
        db_table = 'application'
        managed = True
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'
    


