"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from drf_spectacular.utils import extend_schema

from Blog.views import ProfileViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from djoser.views import UserViewSet
from django.urls import path, include


@extend_schema(tags=['JWT Auth'])
class TokenObtainPairView(TokenObtainPairView):
    pass


@extend_schema(tags=['JWT Auth'])
class TokenRefreshView(TokenRefreshView):
    pass


@extend_schema(tags=['Users'])
class UserViewSet(UserViewSet):
    pass


auth_jwt_urls = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

auth_users_urls = [
    path('', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('<int:pk>/',
         UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='user-detail'),
]

urlpatterns = [
    path('reset/', ProfileViewSet.as_view, name='reset'),
    path('admin/', admin.site.urls),
    path('', include('Blog.urls')),
    path('auth/jwt/', include(auth_jwt_urls)),
    path('auth/users/', include(auth_users_urls)),

    # path('auth/jwt/', include('djoser.urls.jwt')),
    # path('auth/authtoken/auth', include('djoser.urls.authtoken')),
    # path('auth/', include('djoser.urls')),
]
