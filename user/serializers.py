# from rest_framework import serializers

# from .models import User

# class UserSerializer(serializers.ModelSerializer):
#   class Meta:
#       model = User
#       exclude = ('password',)

from rest_framework import serializers
from .models import User

from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
    )

class UserSerializer(serializers.ModelSerializer):
    """
    Creates a new user.
    Email, username, and password are required.
    Returns a JSON web token.
    """

    # The password must be validated and should not be read by the client
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )

    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'token', 'username', 'password',)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
