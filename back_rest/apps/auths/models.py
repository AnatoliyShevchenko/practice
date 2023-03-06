from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from django.core.exceptions import ValidationError
from django.utils import timezone

from functools import cached_property
from typing import Any
from datetime import datetime


class UserManager(BaseUserManager):
    """ClientManager."""

    def create_user(
        self,
        email: str,
        password: str,
        first_name: str,
        last_name: str
    ) -> 'User':

        if not email:
            raise ValidationError('Email required')

        client: 'User' = self.model(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        client.set_password(password)
        client.save(using=self._db)
        return client

    def create_superuser(
        self,
        email: str,
        password: str,
        first_name: str,
        last_name: str
    ) -> 'User':

        client: 'User' = self.model(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        client.is_staff = True
        client.is_superuser = True
        client.set_password(password)
        client.save(using=self._db)
        return client


class User(AbstractBaseUser, PermissionsMixin):
    """User."""

    email: str = models.EmailField(
        max_length=100,
        unique=True,
        verbose_name='почта'
    )
    first_name: str = models.CharField(
        verbose_name='имя',
        max_length=50
    )
    last_name: str = models.CharField(
        verbose_name='фамилия',
        max_length=50
    )
    is_active: bool = models.BooleanField(
        default=True,
        verbose_name='активность'
    )
    is_superuser: bool = models.BooleanField(
        default=False,
        verbose_name='администратор'
    )
    is_staff: bool = models.BooleanField(
        default=False,
        verbose_name='менеджер'
    )
    date_joined: datetime = models.DateTimeField(
        default=timezone.now,
        verbose_name='дата регистрации'
    )
    balance: float = models.DecimalField(
        default=0.0,
        max_digits=8,
        decimal_places=2,
        verbose_name='баланс'
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'first_name',
        'last_name'
    )

    objects = UserManager()

    class Meta:
        ordering = (
            '-date_joined',
        )
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    @cached_property
    def fullname(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return self.email