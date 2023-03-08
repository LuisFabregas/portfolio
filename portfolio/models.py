from django.db import models

# Create your models here.
class project(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(blank=True)
    summary=models.TextField(default=title)
    date=models.CharField(max_length=30)
    members=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

class about(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"

class PostImage(models.Model):
    post = models.ForeignKey(project, default=None, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.post.title