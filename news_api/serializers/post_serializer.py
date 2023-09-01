from rest_framework import serializers
from ..models import Post, User

class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%H:%M %d.%m.%Y", read_only=True)
    author = serializers.SlugRelatedField(
      slug_field='username',
      queryset=User.objects
    )
    

    class Meta:
        model = Post
        fields = ['id','title','text','tags','image','author','author_id','created_at']