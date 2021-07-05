from django.contrib import admin
from .models import Blog, Tag

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'created_on', 'updated_on', 'published_on', 'views', 'published')
    list_filter = ('title', 'author', 'slug', 'created_on', 'updated_on', 'published_on', 'views', 'published')
    fields = ['title', 'author', 'slug', 'body', 'tags', 'published', 'published_on']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)