# Generated by Django 4.0.5 on 2022-06-22 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postjob', '0007_remove_listjob_user_listjob_employer'),
        ('jobapplication', '0002_application_listjob_alter_application_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='deadline',
        ),
        migrations.AddField(
            model_name='application',
            name='employer',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='listjob',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postjob.listjob'),
        ),
    ]
