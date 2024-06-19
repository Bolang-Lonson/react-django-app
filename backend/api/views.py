from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import NoteSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Note

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()   # Looking through all users to make sure we don't recreate an existing one
    serializer_class = UserSerializer     # Tells view what kind of data we need to accept to make a new user
    permission_classes = [AllowAny]     #   specifies who can call this api (Anyone)


class NoteListView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self) -> Note:
        user = self.request.user
        return Note.objects.filter(author=user) #   Displaying a list of notes created by the current logged in user
    
    def perform_create(self, serializer:NoteSerializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)