from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserProfileListCreateView, userProfileDetailView
from .views import *
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # path('', index, name='index'),
    # path('api/v1/post', PostAPIView.as_view(), name='PostAPIView'),
    path('1/', PostAPIView.as_view(), name='PostAPIView'),
    path('post/list/', PostViewSet.as_view({'get': 'list'})),
    path('post/list/<int:pk>/', PostViewSet.as_view({'put': 'update'})),
    path('2/', CategoryAPIView.as_view(), name='CategoryAPIView'),
    # gets all user profiles and create a new profile
    path("all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
    # retrieves profile details of the currently logged in user
    path("profile/<int:pk>", userProfileDetailView.as_view(), name="profile"),


    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
