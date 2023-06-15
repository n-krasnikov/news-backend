from rest_framework import serializers
from ..models import User

class UserSerializer(serializers.ModelSerializer):
    test = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ['email', 'username']