from django.contrib import admin
from .models import qualifications, work, education, project, skills
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.
class CVAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }
admin.site.register(qualifications, CVAdmin)
admin.site.register(work, CVAdmin)
admin.site.register(education, CVAdmin)
admin.site.register(project, CVAdmin)
admin.site.register(skills, CVAdmin)