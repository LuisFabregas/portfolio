from django.db import models

# Create your models here.
class qualifications(models.Model):
    points=models.TextField()
    def __str__(self):
        return 'Highlights of Qualifications'

    class Meta:
        verbose_name= 'Qualification'
        verbose_name_plural= 'Qualifications'

class work(models.Model):
    work_title= models.CharField(max_length=100)
    work_description=models.TextField()
    work_date_location=models.CharField(max_length=100)

    def __str__(self):
        return self.work_title

class education(models.Model):
    university=models.CharField(max_length=100)
    program=models.CharField(max_length=100)
    graduation_date=models.CharField(max_length=100)
    acheivements=models.TextField()

    def __str__(self):
        return self.program


class project(models.Model):
    project_title= models.CharField(max_length=100)
    project_description=models.TextField()
    project_date=models.CharField(max_length=100)
    def __str__(self):
        return self.project_title


class skills(models.Model):
    skill_title=models.CharField(max_length=100)
    skill_list=models.TextField()
    def __str__(self):
        return self.skill_title

    class Meta:
        verbose_name= 'Skill'
        verbose_name_plural= 'Skills'
