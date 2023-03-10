from django.db import models


class AbstractModel(models.Model):
    """Abstract model.
    
    For desription all custom models."""

    datetime_created: bool = models.DateTimeField(
        verbose_name="время создания",
        auto_now_add=True
    )
    datetime_updated: bool = models.DateTimeField(
        verbose_name="время обновления",
        auto_now=True
    )
    datetime_deleted: bool = models.DateTimeField(
        verbose_name="время удаления",
        null=True,
        blank=True
    )

    class Meta:
        abstract = True