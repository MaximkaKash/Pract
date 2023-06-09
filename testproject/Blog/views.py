from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.routers import DefaultRouter

from Blog.models import *
from rest_framework import generics
from .serializers import PostSerializer, CategorySerializer, UserSerializer, ProfileSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from .models import UserProfile
# from .permissions import IsOwnerProfileOrReadOnly
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from djoser.serializers import UserSerializer

from rest_framework.authtoken.models import Token


# def index(request):
#     return render(request, 'Index.html')

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = {
    #     'list': [IsAuthenticatedOrReadOnly],
    #     'create': [IsAuthenticated],
    #     'update': [IsAuthenticated],
    #     'partial_update': [IsAuthenticated],
    #     'destroy': [IsAuthenticated],
    # }


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser, ]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def list(self, request, *args, **kwargs):

        return super().list(request, *args, **kwargs)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [IsOwnerProfileOrReadOnly, ]
    permission_classes = [IsAdminUser, ]
