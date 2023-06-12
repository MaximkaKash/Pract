from drf_spectacular.utils import extend_schema
from rest_framework.mixins import RetrieveModelMixin

from Blog.models import *
from rest_framework import generics, status

from .permissions import *
from .serializers import PostSerializer, CategorySerializer, UserSerializera, ProfileSerializer, CommentSerializer, \
    UserCe
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from .models import UserProfile
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from djoser.serializers import UserSerializer


@extend_schema(tags=['post'])
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (PostPermission,)
    http_method_names = ['get', 'delete', 'put', 'delete']


@extend_schema(tags=['comment'])
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ['get', 'delete', 'put', 'delete']
    permission_classes = (CommentPermission, )

@extend_schema(tags=['category'])
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (CategoryPermission,)
    http_method_names = ['get', 'delete', 'put', 'delete']


@extend_schema(tags=['user'])
class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializera
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    http_method_names = ['get', 'delete', 'put', 'delete']


@extend_schema(tags=['profile'])
class ProfileViewSet(viewsets.ModelViewSet, RetrieveModelMixin):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser, ]
    http_method_names = ['get', 'delete', 'put', 'delete']
    # def retrieve(self, request, *args, **kwargs):

    # @extend_schema(
    #     parameters=[
    #         QuerySerializer,  # serializer fields are converted to parameters
    #         OpenApiParameter("nested", QuerySerializer),  # serializer object is converted to a parameter
    #         OpenApiParameter("queryparam1", OpenApiTypes.UUID, OpenApiParameter.QUERY),
    #         OpenApiParameter("pk", OpenApiTypes.UUID, OpenApiParameter.PATH),  # path variable was overridden
    #     ],
    #     request=YourRequestSerializer,
    #     responses=YourResponseSerializer,
    #     # more customizations
    # )


class UserCre(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserCe
