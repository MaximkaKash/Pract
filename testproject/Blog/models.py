from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

import datetime


class Category(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="Category")


class BaseContent(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Post(BaseContent):
    name = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(null=True, blank=True, verbose_name="Description")
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Comment(BaseContent):
    # author = models.CharField(max_length=30, null=True, blank=True)S
    body = models.TextField(null=True, blank=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_organizer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Log(models.Model):
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    message = models.TextField()

    def __str__(self):
        return self.message


# triggred when User object is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(
            user=instance
        )


# triggred when User object is saved
@receiver(post_save, sender=User)
def log_user_saved(sender, instance, **kwargs):
    Log.objects.create(
        message=f"user {instance.username} is saved"
    )


# triggred when Profile object is saved
@receiver(post_save, sender=UserProfile)
def log_profile_saved(sender, instance, **kwargs):
    Log.objects.create(
        message=f"profile {instance} is saved"
    )
