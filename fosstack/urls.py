from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from filebrowser.sites import site
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)

handler400 = 'back_office.views.bad_request'
handler403 = 'back_office.views.permission_denied'
handler404 = 'back_office.views.page_not_found'
handler500 = 'back_office.views.server_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('back_office.urls')),
    re_path(r'^', include('core_blog.urls')),
    re_path(r'^tinymce/', include('tinymce.urls')),
    re_path(r'^admin/filebrowser/', site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
