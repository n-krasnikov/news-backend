from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostsViewSet, UsersViewSet, AuthViewSet

router = DefaultRouter()
router.register(r'posts', PostsViewSet, basename='posts')
router.register(r'users', UsersViewSet, basename='users')
# router.register(r'auth', AuthViewSet, basename='register')

urlpatterns = [
  path('', include(router.urls)),
  path('auth/signup', AuthViewSet.as_view({'post':'register'})),
  path('auth/signin', AuthViewSet.as_view({'post':'login'}))
]