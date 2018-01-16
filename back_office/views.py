from django.views.generic.edit import CreateView
from django.http import Http404
from django.http import JsonResponse
from django.contrib import sitemaps
from django.views.generic import TemplateView
from django.views import View

from . import forms
from . import models
from core_blog.mixins import PageTitleMixin
from core_blog.models import Post


class CreateContactView(CreateView):
    form_class = forms.ContactForm
    success_url = '/'
    template_name = 'back_office/contact.html'


class PostSitemapView(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Post.objects.active()

    def lastmod(self, obj):
        return obj.updated


class SubscribeView(View):
    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        email_qs = models.Subscribe.objects.filter(email=email)
        if email_qs.exists():
            data = {"status": "404"}
        else:
            data = {"status": "400"}
            models.Subscribe.objects.create(email=email)
        return JsonResponse(data)


class BadRequestView(PageTitleMixin, TemplateView):
    page_title = 'Bad Request'
    template_name = 'error_handler/bad_request.html'


class PermissionDeniedView(PageTitleMixin, TemplateView):
    page_title = 'Permission Denied'
    template_name = 'error_handler/permission_denied.html'


class PageNotFoundView(PageTitleMixin, TemplateView):
    page_title = 'Page Not Found'
    template_name = 'error_handler/page_not_found.html'


class ServerErrorView(PageTitleMixin, TemplateView):
    page_title = 'Server Error'
    template_name = 'error_handler/server_errors.html'
