import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from Blog.models import UserProfile

client = APIClient()


# def get_path(pk):
#     return reverse('profile', kwargs={'pk': pk})

def get_path(pk: int):
    return reverse('profile', kwargs={'pk': pk})


@pytest.mark.django_db
def test_register_user():
    user = User.objects.create_superuser(username='bogdan', password='password')
    userProfile = UserProfile.objects.create(user=user)
    client.force_authenticate(user)
    response = client.get(get_path(user.id))
    print(response.json())
    # assert response.status_code == 200
    # assert response.
