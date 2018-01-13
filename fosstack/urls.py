from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('core_blog.urls')),
    re_path(r'^tinymce/', include('tinymce.urls')),
]
