from django.shortcuts import render
from .models import qualifications, work, education, skills,project
# Create your views here.
def cv(request):
    qualifications_list=qualifications.objects.all()
    work_list=work.objects.all()
    education_list=education.objects.all()
    skills_list=skills.objects.all()
    project_list=project.objects.all()
    template='cv/cv.html'
    context={
        'qualifications':qualifications_list,
        'work_list':work_list,
        'skills':skills_list,
        'education':education_list,
        'project_list':project_list,
    }
    return render(request, template, context)