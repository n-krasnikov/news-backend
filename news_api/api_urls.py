from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.posts import PostsViewSet

router = DefaultRouter()
router.register(r'posts', PostsViewSet, basename='posts')

urlpatterns = [
  path('', include(router.urls))
]