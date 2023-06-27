from rest_framework import serializers
from django.contrib.auth import authenticate

class SignInSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if not email:
            raise serializers.ValidationError(
                'Email required'
            )

        if not password:
            raise serializers.ValidationError(
                'Password required'
            )

        user = authenticate(username=email, password=password)

        if not user:
            raise serializers.ValidationError(
                'User Does not exist'
            )

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }