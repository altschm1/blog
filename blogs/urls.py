from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='index'),
    path('archives/', views.AllBlogListView.as_view(), name='archives'),
    path('about-me/', views.about_me, name='about_me'),
    path('tags/', views.TagListView.as_view(), name='tags'),
    path('<str:blog_slug>/', views.BlogDetailView.as_view(), name='detail'),
    path('tags/<str:tag_slug>/', views.TagDetailView.as_view(), name='tag'),
    
]