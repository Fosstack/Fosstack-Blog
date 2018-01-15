from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from back_office import views as error_handler
from filebrowser.sites import site
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)

handler400 = error_handler.bad_request.as_view()
handler403 = error_handler.permission_denied.as_view()
handler404 = error_handler.page_not_found.as_view()
handler500 = error_handler.server_error.as_view()

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('back_office.urls')),
    re_path(r'^', include('core_blog.urls')),
    re_path(r'^tinymce/', include('tinymce.urls')),
    re_path(r'^admin/filebrowser/', site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
