from django.shortcuts import render
from Blog.models import *
from rest_framework import generics
from .serializers import PostSerializers, CategorySerializers


# def index(request):
#     return render(request, 'Index.html')

class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
