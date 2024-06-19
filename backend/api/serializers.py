from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User   #   the model we intend to serialise (for future json communication)
        fields = ["id", "username", "password"] #   fields we serialise when accepting a new user and returning a user
        extra_kwargs = {
            "password": {"write_only": True}    # Tells django to accept password when creating a user but never return this info
        }

    # Creating our method for creating a new user with the validated data
    def create(self, validated_data:dict) -> User:
        user = User.objects.create_user(**validated_data)
        return user
    

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'author']
        extra_kwargs = {
            'author': {'read_only': True}   #   we should only be able to read who the author is and not write it
        }