from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(title="RentUy API", default_version='v0.1'),
   public=True,
   permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('property/', include(('property.urls', 'property'))),
    path('account/', include(('account.urls', 'account'))),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
