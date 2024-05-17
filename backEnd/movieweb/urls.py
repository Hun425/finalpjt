from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import validate_username,validate_email
urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('profile/', include('accounts.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/user/', include('dj_rest_auth.urls')),
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
    path('validate_username/', validate_username, name='validate_username'),
    path('validate_email/', validate_email, name='validate_email'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
