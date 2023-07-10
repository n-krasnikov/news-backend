from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
import re

from ..serializers import SignUpSerializer
from ..models import User

class AuthViewSet(ModelViewSet):

    def register(self, request):
        user = request.data

        serializer = SignUpSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("OK", status=status.HTTP_201_CREATED)

    def verify(self, request):
        token = request.headers.get('Authorization', None)
        if not token:
            return Response('Unauthorized', status=status.HTTP_401_UNAUTHORIZED)
        
        if not token.startswith('Bearer'):
            return Response('Invalid token', status=status.HTTP_400_BAD_REQUEST)
        
        token = re.sub('Bearer ', '', token)
        try:
            user = User.objects.get(id = AccessToken(token)['user_id'])
        except Exception:
            return Response('User does not exist', status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"user": 
                            {"id": user.id, 
                            "username": user.username, 
                            "email": user.email, 
                            "avatar": user.avatar}
                            }, status=status.HTTP_200_OK)