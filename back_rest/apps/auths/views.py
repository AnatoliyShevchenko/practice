from django.db.models import QuerySet

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request

from .models import User
from .serializers import UserSerializer, UserComicsSerializer

from typing import Optional


class UserView(ViewSet):
    """User View."""

    queryset = User.objects.all()

    def list(self, request: Request) -> Response:
        """GET Method. get all objects."""
        user: QuerySet[User] = self.queryset.all()
        serializer: UserSerializer = \
        UserSerializer(
            user,
            many=True
        )
        return Response(
            {
                'Users': serializer.data
            }
        )

    def retrieve(self, request: Request, pk: str) -> Response:
        """GET Method. get some object."""

        user: Optional[User] = None
        try:
            user = self.queryset.get(
                id=pk
            )
            serializer: UserComicsSerializer = \
            UserComicsSerializer(user)
        except User.DoesNotExist:
            return Response({
                'message': 'error'
            })
        else:
            return Response({
                'data': {
                    'user': serializer.data
                }
            })

