from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()   # Looking through all users to make sure we don't recreate an existing one
    serializer_class = User     # Tells view what kind of data we need to accept to make a new user
    permission_classes = [AllowAny]     #   specifies who can call this api (Anyone)