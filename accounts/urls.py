from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

from .views import *


urlpatterns = [
    path('login/', login_view, name='auth_login'),
    path('register/', register_user, name="register"),
    path("logout/", logout_view, name="auth_logout"),
    path('profile/',profile_view, name='profile'),
    path('upload_image/',upload_image_view, name='upload_image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)