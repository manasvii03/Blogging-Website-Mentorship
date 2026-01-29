from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Favourites, Blog, Reading_List
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

class FavouriteToggleAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, blog_id):
        try:
            blog = Blog.objects.get(id=blog_id)
            favourite_relation = Favourites.objects.get(user=request.user, blog=blog)

            if favourite_relation.exists():
                favourite_relation.delete()
                return Response({"message": "Removed from Favourites", "is_favorite": False}, status=status.HTTP_200_OK)
            else:
                favourite_relation.create(user=request.user, blog=blog)
                return Response({"message": "Added to Favourites", "is_favorite": True}, status=status.HTTP_201_CREATED)
        except Blog.DoesNotExist:
            return Response({"error": "This blog no longer exists."}, status=status.HTTP_404_NOT_FOUND)


class ReadingListAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, blog_id):
        try:
            blog = Blog.objects.get(id=blog_id)
            list_relation = Reading_List.objects.get(user=request.user, blog=blog)

            if list_relation.exists():
                list_relation.delete()
                return Response({"message": "Removed from Reading List", "in_reading_list": False}, status=status.HTTP_200_OK)
            else:
                list_relation.create(user=request.user, blog=blog)
                return Response({"message": "Added to Reading List", "in_reading_list": True}, status=status.HTTP_201_CREATED)
        except Blog.DoesNotExist:
            return Response({"error": "This blog no longer exists."}, status=status.HTTP_404_NOT_FOUND)