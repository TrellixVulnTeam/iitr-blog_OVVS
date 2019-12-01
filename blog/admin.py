from django.contrib.admin import register
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from blog.models import Tag, Blog


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(Tag)
admin.site.register(Blog, BlogAdmin)

# @register(Blog)
# class BlogAdmin(ImportExportModelAdmin):
#     fields = ('title', 'text', 'image', 'tag')
#     list_display = ('title', 'text')
