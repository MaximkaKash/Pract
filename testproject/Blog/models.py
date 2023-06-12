from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


class UserProfile(AbstractUser):
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_organizer = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="Category")

    def __str__(self):
        return self.name


class BaseContent(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Post(BaseContent):
    name = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(null=True, blank=True, verbose_name="Description")
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(BaseContent):
    body = models.TextField(null=True, blank=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, blank=True)

