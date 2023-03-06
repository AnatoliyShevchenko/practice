from django.db.models import QuerySet
from django.contrib.auth import login, logout, authenticate

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request

from .models import User
from .serializers import (
    UserSerializer, 
    UserComicsSerializer,
    RegistrationSerializer,
    LoginSerializer,
)

from typing import Optional

# Create your views here.
class RegistrationView(ViewSet):
    """Registration View."""

    queryset: QuerySet = User.objects.all()

    def create(self, request: Request) -> Response:
        serializer: RegistrationSerializer =\
            RegistrationSerializer(
                data=request.data
            )
        if not serializer.is_valid():
            return Response({
                'error' : serializer.errors
            })
        serializer.save()
        return Response({
            'success' : 'success'
        })
    

class LoginView(ViewSet):
    """Login View."""

    queryset: QuerySet = User.objects.all()

    def create(self, request: Request) -> Response:
        serializer: LoginSerializer =\
            LoginSerializer(
                data=request.data
            )
        if not serializer.is_valid():
            return Response({
                'error' : serializer.errors
            })
        username = serializer.data['username']
        password = serializer.data['password']
        user = authenticate(
            username=username,
            password=password
        )
        login(request, user)
        return Response({
            'message' : 'autorization success'
        })
    

class LogoutView(ViewSet):
    """Logout User."""

    queryset = User.objects.all()

    def list(self, request) -> Response:
        if not request.user:
            return Response({
                'error' : 'not autorized'
            })

        logout(request)
        return Response({
            "message" : "kill"
        })