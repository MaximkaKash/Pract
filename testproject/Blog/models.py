from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="Category")


class Post(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="Main")
    description = models.TextField(null=True, blank=True, verbose_name="Description")
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Comment(models.Model):
    author = models.CharField(max_length=30, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, blank=True)
