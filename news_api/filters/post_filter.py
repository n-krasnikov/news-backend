from django_filters import rest_framework as filters, CharFilter
from django.db.models import Q

from ..models import Post

class PostFilter(filters.FilterSet):
    all = CharFilter(method='all_fields_search', label="Search")
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'] ,
            'text': ['icontains'] ,
            'tags': ['icontains'] ,
            'author__username': ['icontains'],
        }

    def all_fields_search(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(text__icontains=value) | 
            Q(tags__icontains=value) | 
            Q(author__username__icontains=value)
        )