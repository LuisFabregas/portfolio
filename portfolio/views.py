from django.shortcuts import render, get_object_or_404 
from .models import project, about, PostImage
from .forms import ContactForm
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
    projects=project.objects.all()
    aboutme=about.objects.first()
    num_of_projects=project.objects.all().count()
    if request.method == "POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            message = form.cleaned_data['message']+"\n"
            message += "Sent by: "+form.cleaned_data['email'] 
            send_mail(
                sender_name,
                message,
                settings.EMAIL_HOST_USER,
                ['luisfabregas416@gmail.com'],
                )
    else:
        form=ContactForm()  
    context={
        'projects':projects,
        'aboutme':aboutme,
        'num_of_projects':num_of_projects,
        'form':form,
    }
    return render(request, 'portfolio/home.html', context)

def detail(request, project_id):
    project_detail = get_object_or_404(project, pk=project_id)
    projects=project.objects.all()
    photos= PostImage.objects.filter(post=project_detail)
    num_of_projects=project.objects.all().count()
    return render(request, 'portfolio/detail.html', {
        'project': project_detail,
        'photos':photos,
        'projects':projects,
        'num_of_projects':num_of_projects,
        })

