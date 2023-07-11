from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from ..models import Post
from ..serializers import PostSerializer

class PostsViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer