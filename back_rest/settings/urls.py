from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from rest_framework.routers import DefaultRouter

from auths.views import (
    RegistrationView, 
    LoginView,
    LogoutView,
)
from marvel.views import ComicsView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
router: DefaultRouter = DefaultRouter(
    trailing_slash=True
)
router.register('comics', ComicsView)
router.register('registration', RegistrationView)
router.register('login', LoginView)
router.register('logout', LogoutView)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]

urlpatterns += [
    path('api/v1/', include(router.urls))
]