from rest_framework import serializers

from django.db.models import QuerySet
from django.contrib.auth.hashers import make_password, check_password

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
    

class RegistrationSerializer(serializers.ModelSerializer):
    """Registration Serializer."""

    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
            'password2'
        )

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError(
                'passwords not match'
            )
        return super().validate(attrs)

    def save(self, **kwargs):
        user = User.objects.create(
            email = self.data.get('email'),
            first_name = self.data.get('first_name'),
            last_name = self.data.get('last_name'),
            password = make_password(self.data.get('password'))
        )
        return user