# Python
from typing import Optional

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.handlers.wsgi import WSGIRequest

from .models import User


class ClientAdmin(UserAdmin):
    model = User

    fieldsets = (
        ('Information', {
            'fields': (
                'email',
                'password',
                'date_joined',
                'first_name',
                'last_name'
            )
        }),
        ('Permissions', {
            'fields': (
                'is_superuser',
                'is_staff',
                'is_active',
            )
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': (
                'wide',
            ),
            'fields': (
                'first_name',
                'last_name',
                'email',
                'password1',
                'password2',
                'is_active'
            ),
        }),
    )
    search_fields = (
        'email',
    )
    readonly_fields = (
        'date_joined',
        'is_superuser',
        'is_staff',
        'is_active'
    )
    list_display = (
        'email',
        'password',
        'first_name',
        'last_name',
        'date_joined',
        'is_superuser',
        'is_staff',
        'is_active'
    )
    list_filter = (
        'email',
        'is_superuser',
        'is_staff',
        'is_active'
    )
    ordering = (
        'email',
    )

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[User] = None
    ) -> tuple:
        if not obj:
            return self.readonly_fields

        return self.readonly_fields + (
            'email',
        )


admin.site.register(User, ClientAdmin)
