from rest_framework import serializers
from Blog.models import Post, Category


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "name", "category")


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")
