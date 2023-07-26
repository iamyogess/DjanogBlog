from django.contrib import admin
from . models import AddBlogModel

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ['id','title','blog_content','blog_img']

admin.site.register(AddBlogModel, BlogAdmin)
