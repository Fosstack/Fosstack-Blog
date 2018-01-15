from django.urls import path
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap

from . import views

app_name = 'back_office'

sitemaps = {
    'posts':  views.PostSitemap,
}

urlpatterns = [
    path('contact', views.CreateContactView.as_view(), name='contact'),
    path('robots.txt', lambda r: HttpResponse(
        'User-agent: *\nDisallow:', content_type="text/plain")
    ),
    path('subscribe', views.Subscribe.as_view(), name='subscribe'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]
