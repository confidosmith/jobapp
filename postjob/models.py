from email.policy import default
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from userprofile.models import EmployerProfile

# Create your models here.


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
    