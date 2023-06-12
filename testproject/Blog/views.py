from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import permission_classes, api_view
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.routers import DefaultRouter

from Blog.models import *
from rest_framework import generics, status
from .serializers import PostSerializer, CategorySerializer, UserSerializer, ProfileSerializer, CommentSerializer, \
    UserCe
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from .models import UserProfile
# from .permissions import IsOwnerProfileOrReadOnly
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from djoser.serializers import UserSerializer
from django.core.mail import send_mail
from rest_framework.authtoken.models import Token
from django.shortcuts import redirect


@extend_schema(tags=['post'])
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get', 'delete', 'put']

    # def list(self, request, *args, **kwargs):
    #     try:
    #         send_mail(
    #             subject='Add an eye-catching subject',
    #             message='asad',
    #             from_email='some@mail.ru',
    #             recipient_list=['maximkanashyts@gmail.com', ])
    #     except Exception as err:
    #         print(err)
    #     return super().list(request)


@extend_schema(tags=['comment'])
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ['get', 'delete', 'put']
    # permission_classes = {
    #     'list': [IsAuthenticatedOrReadOnly],
    #     'create': [IsAuthenticated],
    #     'update': [IsAuthenticated],
    #     'partial_update': [IsAuthenticated],
    #     'destroy': [IsAuthenticated],
    # }


@extend_schema(tags=['category'])
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny, ]
    http_method_names = ['get', 'delete', 'put']

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            # Получение объекта из базы данных по заданному 'pk'
            instance = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

            # Создание сериализатора для объекта
        serializer = CategorySerializer(instance)

        # Возвращение сериализованных данных в качестве ответа
        return Response(serializer.data, status=status.HTTP_200_OK)


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly, ]
#     http_method_names = ['get', 'delete', 'put']
#
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)

@extend_schema(tags=['profile'])
class ProfileViewSet(viewsets.ModelViewSet, RetrieveModelMixin):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [IsOwnerProfileOrReadOnly, ]
    permission_classes = [IsAdminUser, ]
    http_method_names = ['get', 'delete', 'put']
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
