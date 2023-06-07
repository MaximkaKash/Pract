from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="Category")


class BaseContent(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Post(BaseContent):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="Main")
    description = models.TextField(null=True, blank=True, verbose_name="Description")
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Comment(BaseContent):
    # author = models.CharField(max_length=30, null=True, blank=True)S
    body = models.TextField(null=True, blank=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, blank=True)


class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_organizer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
