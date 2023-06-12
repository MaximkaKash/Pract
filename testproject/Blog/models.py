from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth import get_user_model
import datetime


class UserProfile(AbstractUser):
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_organizer = models.BooleanField(default=False)

class Category(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="Category")

    def __str__(self):
        return self.name


class BaseContent(models.Model):
    author = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
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
    # author = models.CharField(max_length=30, null=True, blank=True)S
    body = models.TextField(null=True, blank=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, blank=True)





class Log(models.Model):
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    message = models.TextField()

    def __str__(self):
        return self.message


