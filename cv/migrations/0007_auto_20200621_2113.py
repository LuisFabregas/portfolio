# Generated by Django 3.0.7 on 2020-06-22 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0006_remove_work_work_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_date_location',
            new_name='project_date',
        ),
    ]
