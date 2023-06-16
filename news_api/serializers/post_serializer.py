from rest_framework import serializers
from ..models import Post, User

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
      slug_field='username',
      queryset=User.objects
    )

    class Meta:
        model = Post
        fields = ['id','title','text','tags','image','author','author_id']