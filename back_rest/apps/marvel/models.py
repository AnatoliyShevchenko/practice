from django.db import models

from auths.models import User
from abstracts.models import AbstractModel


class Genre(AbstractModel, models.Model):
    """Genre model for comics."""

    title: str = models.CharField(
        verbose_name='название',
        max_length=60
    )

    class Meta:
        ordering = (
            'id',
        )
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'

    def __str__(self) -> str:
        return f'{self.title}'
        

class Comics(AbstractModel, models.Model):
    """Marvel comics model."""

    title: str = models.CharField(
        verbose_name='название',
        max_length=120,
        null=True
    )
    pages: int = models.PositiveSmallIntegerField(
        verbose_name='количество страниц'
    )
    genres: Genre = models.ManyToManyField(
        verbose_name='жанр',
        related_name='comics',
        to=Genre,
    )
    author: User = models.ForeignKey(
        verbose_name='автор',
        to=User,
        on_delete=models.RESTRICT,
        related_name='comics'
    )
    cost: int = models.PositiveSmallIntegerField(
        verbose_name='цена'
    )
    
    class Meta:
        ordering = (
            'pages',
        )
        verbose_name = 'комикс'
        verbose_name_plural = 'комиксы'

    def __str__(self) -> str:
        return f'{self.author} | {self.pages}'