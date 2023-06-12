from django.core.mail import send_mail
from rest_framework import serializers
from Blog.models import Post, Category, UserProfile, Comment
from django.contrib.auth.models import User
from djoser.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


# class UserSerializer(serializers.ModelSerializer):
#     # user = serializers.StringRelatedField(read_only=True)
#
#     class Meta:
#         model = UserProfile
#         fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class UserCe(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )
        try:
            send_mail(
                subject='Add an eye-catching subject',
                message='asad',
                from_email='maximkanashyts@gmail.com',
                recipient_list=['maximkanashyts@gmail.com', ], )
        except Exception as err:
            print(err)
        return user
