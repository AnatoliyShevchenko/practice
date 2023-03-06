from rest_framework import serializers

from .models import Comics, Genre


class ComicsSerializer(serializers.ModelSerializer):
    """PlayerSerializer."""
    
    id = serializers.IntegerField()
    title = serializers.CharField()
    pages = serializers.IntegerField()
    genres = serializers.CharField()
    author = serializers.CharField()
    cost = serializers.IntegerField()

    class Meta:
        model = Comics
        fields = '__all__'