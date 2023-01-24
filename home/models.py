from django.db import models
from django.contrib.auth.models import User
from userprofile.models import EmployerProfile
from userprofile.models import EmployeeProfile
# Create your models here.


class ConfidoJobinfo(models.Model):
    name = models.CharField(max_length=50)
    keyword = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to= 'logo', blank=True, null=True)
    favicon = models.ImageField(upload_to= 'logo', blank=True, null=True)
    banner1 = models.ImageField(upload_to= 'banner', blank=True, null=True)
    banner2 = models.ImageField(upload_to= 'banner', blank=True, null=True)
    email = models.EmailField()
    website = models.URLField(max_length=50)
    copyright_year = models.CharField(max_length=50)

    def __str__(self):
        return self.name 

class Category(models.Model):
    category = models.CharField(max_length= 150)

    def __str__(self):
        return self.category 

    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

        

class Listjob(models.Model):
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    job_location = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.CharField(max_length=100, null=True, blank=True)
    salary = models.CharField(max_length=50)
    deadline = models.DateField()
    logo = models.ImageField(upload_to='logo', default='avatar.jpg', null=True, blank=True) 
    website = models.URLField(null=True, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(null=True, blank=True)
    display = models.BooleanField(null=True, blank=True, default=True)
    closed = models.BooleanField(null=True, blank=True)
    featured = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.job_title 

    class Meta:
        db_table = 'listjob'
        managed = True
        verbose_name = 'Listjob'
        verbose_name_plural = 'Listjob'
    
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
    

