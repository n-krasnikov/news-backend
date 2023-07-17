from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from ..models import User, Post
from ..serializers import UserSerializer, PostSerializer

class UsersViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk):
        if not pk.isdigit():
            return Response("Invalid ID", status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(pk=pk)
            posts = Post.objects.filter(author=pk)
            user_serializer = UserSerializer(user)
            post_serializer = PostSerializer(posts, many=True)
            return Response({"user": user_serializer.data, "posts": post_serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({"detail": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

    