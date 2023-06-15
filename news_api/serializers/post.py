from rest_framework import serializers
from ..models import Post, User

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    text = serializers.CharField()
    tags = serializers.CharField(max_length=255)
    image = serializers.CharField(max_length=255)
    author_id = serializers.IntegerField()

    author = serializers.SlugRelatedField(
      slug_field='username',
      queryset=User.objects
    )

class UserSerializer(serializers.ModelSerializer):
    test = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ['email', 'username']