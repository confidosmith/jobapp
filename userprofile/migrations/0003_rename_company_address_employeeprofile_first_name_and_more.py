# Generated by Django 4.0.5 on 2022-06-09 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_remove_employerprofile_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeprofile',
            old_name='company_address',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='employeeprofile',
            old_name='company_name',
            new_name='last_name',
        ),
    ]
