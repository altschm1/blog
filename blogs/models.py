import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    slug = models.SlugField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=240, blank=False)
    author = models.CharField(max_length=240, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    published_on = models.DateTimeField(null=True)
    slug = models.SlugField(max_length=50, unique=True)
    views = models.IntegerField(default=0)
    body = models.TextField()
    published = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def publish_blog(self):
        self.published = True
        self.published_on = timezone.now()
        

