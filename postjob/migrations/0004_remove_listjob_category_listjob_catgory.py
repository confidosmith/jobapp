# Generated by Django 4.0.5 on 2022-06-20 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postjob', '0003_alter_listjob_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listjob',
            name='category',
        ),
        migrations.AddField(
            model_name='listjob',
            name='catgory',
            field=models.CharField(default='a', max_length=150),
        ),
    ]
