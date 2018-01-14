from django.views.generic.edit import CreateView
from django.contrib import sitemaps
from . import forms
from core_blog.models import Post


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
