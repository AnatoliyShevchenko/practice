from django.contrib import admin

from .models import (
    Genre,
    Comics,
)


class GenreAdmin(admin.ModelAdmin):
    """Admin for genres model."""

    model = Genre

    list_display: tuple = (
        'title',
    )
    readonly_fields: tuple = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
    )

class ComicsAdmin(admin.ModelAdmin):
    """Admin for comics model."""

    model = Comics

    list_display: tuple = (
        'title',
        'pages',
        'author',
        'cost',
    )
    readonly_fields: tuple = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
    )

admin.site.register(Genre, GenreAdmin)
admin.site.register(Comics, ComicsAdmin)