from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from ..models import Post, User
from ..serializers import PostSerializer

class PostsViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
