from django.contrib.auth.models import User
from rest_framework import serializers

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