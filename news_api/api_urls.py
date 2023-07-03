from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import PostsViewSet, UsersViewSet, AuthViewSet

router = DefaultRouter()
router.register(r'posts', PostsViewSet, basename='posts')
router.register(r'users', UsersViewSet, basename='users')

urlpatterns = [
  path('', include(router.urls)),
  path('auth/signup', AuthViewSet.as_view({'post': 'register'})),
  path('auth/signin', TokenObtainPairView.as_view(), name='sign_in'),
  path('auth/refresh', TokenRefreshView.as_view(), name='refresh'),
  path('auth/verify', AuthViewSet.as_view({'get': 'verify'}))
]