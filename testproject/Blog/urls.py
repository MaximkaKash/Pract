from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileListCreateView, userProfileDetailView
from .views import *
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'categorys', CategoryViewSet)

urlpatterns = [
    # path('', index, name='index'),
    path('api/', include(router.urls)),
    path('api/', include(router.urls)),
    # gets all user profiles and create a new profile
    path("all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
    # retrieves profile details of the currently logged in user
    path("profile/<int:pk>", userProfileDetailView.as_view(), name="profile"),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
