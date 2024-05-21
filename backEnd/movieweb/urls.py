from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import validate_username,validate_email
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import CustomRegisterView,GPTChatView
from . import views
schema_view = get_schema_view(
   openapi.Info(
      title="Your Project API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourproject.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
   path('admin/', admin.site.urls),
   path('movies/', include('movies.urls')),
   path('profile/', include('accounts.urls')),
   path('accounts/', include('dj_rest_auth.urls')),
   path('accounts/user/', include('dj_rest_auth.urls')),
   path('accounts/signup/', CustomRegisterView.as_view()),
   path('validate_username/', validate_username, name='validate_username'),
   path('validate_email/', validate_email, name='validate_email'),
#  re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('api/v1/', include('dj_rest_auth.urls')),
   path('gpt/chat/',GPTChatView.as_view(), name='gpt_chat'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
