# Generated by Django 3.0.7 on 2020-06-21 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_auto_20200621_1233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='qualifications',
            options={'verbose_name': 'Qualification', 'verbose_name_plural': 'Qualifications'},
        ),
        migrations.AlterModelOptions(
            name='skills',
            options={'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
        migrations.AddField(
            model_name='work',
            name='work_location',
            field=models.CharField(default='unknown date', max_length=100),
        ),
    ]
