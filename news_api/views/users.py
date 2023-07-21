from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from ..models import User, Post
from ..serializers import UserSerializer, PostSerializer
from ..utils import save_image, is_image

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
        
    def partial_update(self, request, pk):
        if not pk.isdigit():
            return Response({"detail": "Invalid ID"}, status.HTTP_400_BAD_REQUEST)

        request.data._mutable = True

        avatar = request.FILES.get('avatar')
        path = User.objects.get(pk=pk).avatar

        if avatar is not None:
            if not is_image(avatar):
                return Response({"detail": ".png, .jpg, .svg files only"}, status=status.HTTP_400_BAD_REQUEST)
    
            path = save_image(avatar, "avatars/")

        request.data.update({"username": request.data.get("username")})
        request.data.update({"avatar": path})

        return super().partial_update(request, pk)
    