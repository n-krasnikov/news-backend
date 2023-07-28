from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Post
from ..serializers import PostSerializer
from ..filters import PostFilter
from ..utils import save_image, is_image

class PostsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter
    search_fields = ['author', 'text', 'title', 'tags']

    def create(self, request, *args, **kwargs):
        request.data._mutable = True

        image = request.FILES.get('image')
        path = None

        if image is not None:
            if not is_image(image):
                return Response({"detail": ".png, .jpg, .svg files only"}, status=status.HTTP_400_BAD_REQUEST)
            
            path = save_image(image, "posts/")

        request.data.update({"author": request.user.username})
        request.data.update({"image": path})

        return super().create(request)
  