from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Favourites
from .serializers import UserSerializer, FavouritesSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from posts.models import Blog
from posts.serializers import BlogSerializer
# Create your views here.

class LoginAPIView(APIView):
    def post(self, request):
        user = authenticate(
            username = request.data.get('username'),
            password = request.data.get('password')
        )

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'username': user.username, 'message': 'Login Successful'}, status=status.HTTP_200_OK)
        elif User.objects.filter(username=request.data.get('username')).exists():
            return Response({'error': 'Incorrect Password'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'User not found'}, status=status.HTTP_401_UNAUTHORIZED)

class SignUpAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LikeToggleAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, blog_id):
        try:
            blog = Blog.objects.get(id=blog_id)
            user = request.user

            if user in blog.likes.all():
                blog.likes.remove(user)
                return Response({"message": "Unliked"}, status=status.HTTP_200_OK)
            else:
                blog.likes.add(user)
                return Response({"message": "Liked"}, status=status.HTTP_201_CREATED)
        except Blog.DoesNotExist:
            return Response({"error": "Blog Not Found"}, status=status.HTTP_404_NOT_FOUND)


class BookmarkToggleAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, blog_id):
        try:
            blog = Blog.objects.get(id=blog_id)
            user = request.user

            if user in blog.bookmarks.all():
                blog.bookmarks.remove(user)
                return Response({"message": "Removed from Bookmarks"}, status=status.HTTP_200_OK)
            else:
                blog.bookmarks.add(user)
                return Response({"message": "Added to Bookmarks"}, status=status.HTTP_201_CREATED)
        except Blog.DoesNotExist:
            return Response({"error": "Blog Not Found"}, status=status.HTTP_404_NOT_FOUND)


class LikedBlogsAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        liked_blogs = user.liked_blogs.all()
        liked_data = BlogSerializer(liked_blogs, many=True).data

        return Response({
            'user': user.username,
            'liked_blogs': liked_data,
        })

class BookmarkedBlogsAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        bookmarked_blogs = user.bookmarked_blogs.all()
        bookmarked_data = BlogSerializer(bookmarked_blogs, many=True).data

        return Response({
            'user': user.username,
            'bookmarked_blogs': bookmarked_data,
        })


class FavouriteToggleAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, blog_id):
        try:
            blog = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return Response({"error": "Blog Not Found"}, status=status.HTTP_404_NOT_FOUND)
        fav_query = Favourites.objects.filter(user=request.user, blog=blog)

        if fav_query.exists():
            fav_query.delete()
            return Response({'message':'Removed from Favourites', 'is_favourite':False}, status=status.HTTP_200_OK)
        else:
            Favourites.objects.create(user=request.user, blog=blog)
            return Response({'message':'Added to Favourites', 'is_favourite':True}, status=status.HTTP_201_CREATED)

class FavouritesListAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        my_favs = Favourites.objects.filter(user=request.user)
        serializer = FavouritesSerializer(my_favs, many=True)
        return Response(serializer.data)