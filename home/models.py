from django.db import models

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

    class Meta:
        db_table = 'confidojobinfo'
        managed = True
        verbose_name = 'ConfidoJobinfo'
        verbose_name_plural = 'ConfidoJobinfo'
    
