# Generated by Django 3.0.7 on 2020-06-22 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0005_auto_20200621_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='work_location',
        ),
    ]
