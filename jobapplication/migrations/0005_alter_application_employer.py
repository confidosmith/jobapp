# Generated by Django 4.0.5 on 2022-06-22 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0014_delete_move'),
        ('jobapplication', '0004_alter_application_employer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.employerprofile'),
        ),
    ]
