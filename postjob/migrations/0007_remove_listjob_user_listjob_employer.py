# Generated by Django 4.0.5 on 2022-06-21 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0014_delete_move'),
        ('postjob', '0006_alter_listjob_category_alter_listjob_closed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listjob',
            name='user',
        ),
        migrations.AddField(
            model_name='listjob',
            name='employer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='userprofile.employerprofile'),
        ),
    ]
