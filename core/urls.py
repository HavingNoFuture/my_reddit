from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from core import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reddit.urls')),
    path('profile/', include('profile.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, documenmt_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)