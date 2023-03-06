from rest_framework import serializers

from django.db.models import QuerySet

from .models import User
from marvel.models import Comics


class UserSerializer(serializers.ModelSerializer):
    """PlayerSerializer."""
    
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    date_joined = serializers.DateTimeField()
    balance = serializers.FloatField()

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'date_joined',
            'balance',
            'fullname'
        )
    
class UserComicsSerializer(serializers.ModelSerializer):
    """For view comics user"""

    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'comics'
        )

    def get_comics(self, id):
        comics: QuerySet = Comics.objects.filter(id=id).values('title')
        return comics