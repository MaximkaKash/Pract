import pytest
from django.contrib.auth.models import User
from django.contrib.sites import requests
from django.urls import reverse
from rest_framework.test import APIClient
from Blog.models import UserProfile
from django.test import TestCase
from Blog.models import *

client = APIClient()


# def get_path(pk):
#     return reverse('profile', kwargs={'pk': pk})

def get_path(pk: int):
    return reverse('users/', kwargs={'pk': pk})


@pytest.mark.django_db
def test_register_user():
    user = User.objects.create_superuser(username='bogdan', password='password')
    # userProfile = UserProfile.objects.create(user=user)
    client.force_authenticate(user)
    # response =
    # assert response.
    # print(response)
    # assert response.status_code == 200
    # assert response.
