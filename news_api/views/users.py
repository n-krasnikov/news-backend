import os

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

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
        
    def partial_update(self, request, pk):
        if not pk.isdigit():
            return Response({"detail": "Invalid ID"}, status.HTTP_400_BAD_REQUEST)

        if (request.user.id != int(pk)):
            return Response({"detail": "Access Denied"}, status.HTTP_403_FORBIDDEN)

        request.data._mutable = True

        avatar = request.FILES.get('avatar')
        path = User.objects.get(pk=pk).avatar
        print(path)

        if avatar is not None:
            if not avatar.name.lower().endswith(('.png', '.jpg', '.jpeg', '.svg')):
                return Response({"detail": ".png, .jpg, .svg files only"}, status=status.HTTP_400_BAD_REQUEST)
            
            image_path = settings.STATIC_ROOT + "avatars/" + pk + avatar.name

            path = (
                settings.BACKEND_URL 
                + settings.BACKEND_PORT 
                + settings.STATIC_URL 
                + os.path.relpath(image_path, start = settings.STATIC_ROOT)
            )
            
            with open(image_path, 'wb') as f:
                f.write((avatar.file).read())

        request.data.update({"username": request.data.get("username")})
        request.data.update({"avatar": path})

        return super().partial_update(request, pk)
    