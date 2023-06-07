from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserProfileListCreateView, userProfileDetailView
from .views import *

urlpatterns = [
    # path('', index, name='index'),
    # path('api/v1/post', PostAPIView.as_view(), name='PostAPIView'),
    path('api1/', PostAPIView.as_view(), name='PostAPIView'),
    path('api2/', CategoryAPIView.as_view(), name='CategoryAPIView'),
    # gets all user profiles and create a new profile
    path("all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
    # retrieves profile details of the currently logged in user
    path("profile/<int:pk>", userProfileDetailView.as_view(), name="profile"),
]

