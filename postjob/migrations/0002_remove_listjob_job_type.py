# Generated by Django 4.0.5 on 2022-06-14 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postjob', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listjob',
            name='job_type',
        ),
    ]
