from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from ..serializers import SignUpSerializer, SignInSerializer

class AuthViewSet(ModelViewSet):

    def register(self, request):
        user = request.data

        serializer = SignUpSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def login(self, request):
        user = request.data

        serializer = SignInSerializer(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)