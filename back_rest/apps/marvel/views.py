from django.db.models import QuerySet

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Genre, Comics
from .serializers import ComicsSerializer


class ComicsView(ViewSet):
    """Comics View."""

    queryset = Comics.objects.all()

    def list(self, request: Request) -> Response:
        """GET Method. get all objects."""

        comics: QuerySet[Comics] = self.queryset.all()
        serializer: ComicsSerializer = \
            ComicsSerializer(
                comics,
                many=True
            )
        return Response(
            data={
                'Comics': serializer.data
            },
            status=200
        )

    def retrieve(self, request: Request, pk: str) -> Response:
        """GET Method. get all objects."""
        
        comics: Comics = Comics.objects.get(id=pk)
        serializer: ComicsSerializer = \
            ComicsSerializer(
                comics
            )
        return Response(
            data={
                'Comics': serializer.data
            },
            status=200
        )

