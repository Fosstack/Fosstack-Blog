from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings

from filebrowser.sites import site


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('core_blog.urls')),
    re_path(r'^tinymce/', include('tinymce.urls')),
    re_path(r'^admin/filebrowser/', site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
