from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Favourites
from posts.serializers import BlogSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class FavouritesSerializer(serializers.ModelSerializer):
    blog = BlogSerializer(read_only=True)

    class Meta:
        model = Favourites
        fields = ['id', 'blog', 'created_at']