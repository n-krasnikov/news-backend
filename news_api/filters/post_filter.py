from django_filters import rest_framework as filters

from ..models import Post

class PostFilter(filters.FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'] ,
            'text': ['icontains'] ,
            'tags': ['icontains'] ,
            'author__username': ['icontains'],
        }
