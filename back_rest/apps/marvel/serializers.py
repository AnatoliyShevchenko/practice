from rest_framework import serializers

from django.db.models.query import QuerySet

from typing import (
    Optional,
)

from .models import (
    Comics,
    Genre,
)


class ComicsSerializer(serializers.ModelSerializer):
    """PlayerSerializer."""
    
    id = serializers.IntegerField()
    title = serializers.CharField()
    pages = serializers.IntegerField()
    genres = serializers.SerializerMethodField(method_name='get_genres')
    author = serializers.CharField()
    cost = serializers.IntegerField()

    class Meta:
        model = Comics
        fields = '__all__'

    def get_genres(self, obj: Comics):
        data: list[Optional[Genre]] = []
        queryset: QuerySet[Genre] = obj.genres.all()
        for genre in queryset:
            data.append(genre.title)
        return data