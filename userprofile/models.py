from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EmployerProfile(models.Model):
    company = models.OneToOneField(User, on_delete= models.CASCADE)
    company_address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    website = models.URLField()
    email = models.EmailField()


    def __str__(self):
        return self.company.username


    class Meta:
        db_table = 'employerprofile'
        managed = True
        verbose_name = 'EmployerProfile'
        verbose_name_plural = 'EmployerProfile'


class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.user.username 


    class Meta:
        db_table = 'employeeprofile'
        managed = True
        verbose_name = 'EmployeeProfile'
        verbose_name_plural = 'EmployeeProfile'

