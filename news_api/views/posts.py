from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
import os
from time import time
from django.conf import settings

from ..models import Post
from ..serializers import PostSerializer

class PostsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        request.data._mutable = True

        image = request.FILES.get('image')
        rel_path = None

        if image is not None:
            image_path = settings.STATIC_ROOT + "images/" + str(time()) + image.name

            rel_path = (
                settings.BACKEND_URL 
                + settings.BACKEND_PORT 
                + settings.STATIC_URL 
                + os.path.relpath(image_path, start = settings.STATIC_ROOT)
            )
            
            with open(image_path, 'xb') as f:
                f.write((image.file).read())

        request.data.update({"author": request.user})
        request.data.update({"image": rel_path})

        return(super().create(request))
  
