from django.contrib import admin
from .models import project, about, PostImage
# Register your models here.
admin.site.register(about)

class PostImageAdmin(admin.StackedInline):
    model=PostImage

@admin.register(project)
class projectAdmin(admin.ModelAdmin):
    inlines=[PostImageAdmin]

    class Meta:
        model=project
@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass