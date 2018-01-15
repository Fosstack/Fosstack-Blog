from django.views.generic.edit import CreateView
from django.contrib import sitemaps
from . import forms
from . import models
from core_blog.models import Post
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView

from core_blog.mixins import PageTitleMixin, CsrfExemptMixin


class CreateContactView(CreateView):
    form_class = forms.ContactForm
    success_url = '/'
    template_name = 'back_office/contact.html'


class PostSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Post.objects.active()

    def lastmod(self, obj):
        return obj.updated


def Subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        email_qs = models.Subscribe.objects.filter(email=email)
        if email_qs.exists():
            data = {"status": "404"}
            return JsonResponse(data)
        else:
            data = {"status": "400"}
            models.Subscribe.objects.create(email=email)
    return redirect('/')


class bad_request(CsrfExemptMixin, PageTitleMixin, TemplateView):
    page_title = 'Bad Request'
    template_name = 'error_handler/bad_request.html'


class permission_denied(CsrfExemptMixin, PageTitleMixin, TemplateView):
    page_title = 'Permission Denied'
    template_name = 'error_handler/permission_denied.html'


class page_not_found(CsrfExemptMixin, PageTitleMixin, TemplateView):
    page_title = 'Page Not Found'
    template_name = 'error_handler/page_not_found.html'


class server_error(CsrfExemptMixin, PageTitleMixin, TemplateView):
    page_title = 'Server Error'
    template_name = 'error_handler/server_errors.html'
