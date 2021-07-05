from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog, Tag

class BlogListView(ListView):
    queryset = Blog.objects.filter(published=True).order_by('-published_on')[:15]
    context_object_name = 'blogs_list'
    template_name = 'blogs/index.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogs/detail.html'

    def get_object(self, queryset=None):
        return Blog.objects.get(slug=self.kwargs.get('blog_slug'))

class AllBlogListView(ListView):
    queryset = Blog.objects.filter(published=True).order_by('-published_on')
    context_object_name = 'blogs_list'
    template_name = 'blogs/index.html'

class TagDetailView(DetailView):
    model = Tag
    template_name = 'blogs/tag.html'

    def get_object(self, queryset=None):
        return Tag.objects.get(slug=self.kwargs.get('tag_slug'))

class TagListView(ListView):
    model = Tag
    template_name = 'blogs/tags.html'
    context_object_name = 'tags_list'

def about_me(request):
    return render(request, 'blogs/aboutme.html')