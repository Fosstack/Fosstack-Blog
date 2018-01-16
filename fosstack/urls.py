from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)

from filebrowser.sites import site
from back_office import views as error_handler


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


handler400 = error_handler.BadRequestView.as_view()
handler403 = error_handler.PermissionDeniedView.as_view()
handler404 = error_handler.PageNotFoundView.as_view()
handler500 = error_handler.ServerErrorView.as_view()
