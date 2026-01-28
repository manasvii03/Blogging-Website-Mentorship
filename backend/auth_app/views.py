from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.views import APIView

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