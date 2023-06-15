from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from ..models import Post, User
from ..serializers import PostSerializer

class PostsViewSet(ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def list(self, _):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)