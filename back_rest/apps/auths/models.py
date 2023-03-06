from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from django.core.exceptions import ValidationError
from django.utils import timezone

from typing import Any


# Create your models here.
class UserManager(BaseUserManager):
    """ClientManager."""

    def create_user(
        self,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        username: str
    ) -> 'User':

        if not email:
            raise ValidationError('Email required')

        client: 'User' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        client.username = username
        client.first_name = first_name
        client.last_name = last_name
        client.set_password(password)
        client.save(using=self._db)
        return client

    def create_superuser(
        self,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        username: str
    ) -> 'User':

        client: 'User' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        client.username = username
        client.first_name = first_name
        client.last_name = last_name
        client.is_staff = True
        client.is_superuser = True
        client.set_password(password)
        client.save(using=self._db)
        return client


class User(AbstractBaseUser, PermissionsMixin):
    """User."""

    username = models.CharField(
        max_length=20,
        verbose_name='имя пользователя',
        unique=True
    )
    email = models.EmailField(
        max_length=100,
        unique=True,
        verbose_name='почта'
    )
    first_name = models.CharField(
        verbose_name='имя',
        max_length=50
    )
    last_name = models.CharField(
        verbose_name='фамилия',
        max_length=50
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='активность'
    )
    is_superuser = models.BooleanField(
        default=False,
        verbose_name='администратор'
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name='менеджер'
    )
    date_joined = models.DateTimeField(
        default=timezone.now,
        verbose_name='дата регистрации'
    )
    balance = models.DecimalField(
        default=0.0,
        verbose_name='баланс',
        max_digits=8,
        decimal_places=2
    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = UserManager()

    class Meta:
        ordering = (
            '-date_joined',
        )
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    # def save(
    #     self,
    #     *args: Any,
    #     **kwargs: Any
    # ) -> None:
    #     self.full_clean()
    #     super().save(*args, **kwargs)

    @property
    def fullname(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return self.email