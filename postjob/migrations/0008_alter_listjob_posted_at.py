# Generated by Django 4.0.5 on 2022-06-23 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postjob', '0007_remove_listjob_user_listjob_employer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listjob',
            name='posted_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
