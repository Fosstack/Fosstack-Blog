from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView

from . import forms
from . import models
from .mixins import IsStaffUserMixin, PageTitleMixin, CsrfExemptMixin


class ListPostView(CsrfExemptMixin, ListView):
    model = models.Post
    context_object_name = 'posts'
    template_name = 'core_blog/list_posts.html'

    def get_queryset(self):
        return self.model.objects.select_related('author').all()


class PostDetailView(PageTitleMixin, DetailView):
    model = models.Post
    context_object_name = 'post'
    template_name = 'core_blog/post_detail.html'

    def get_page_title(self):
        post = self.get_object()
        return post.title


class CreatePostView(IsStaffUserMixin, PageTitleMixin, CreateView):
    form_class = forms.CreatePostForm
    success_url = '/'
    page_title = 'Create Awesome Post'
    template_name = 'core_blog/post_form.html'


class AboutView(CsrfExemptMixin, PageTitleMixin, TemplateView):
    page_title = 'About'
    template_name = 'core_blog/about.html'


class PostUpdateView(IsStaffUserMixin, PageTitleMixin, UpdateView):
    model = models.Post
    fields = '__all__'
    context_object_name = 'post'
    template_name = 'core_blog/post_form.html'

    def get_page_title(self):
        post = self.get_object()
        return 'Update {}'.format(post.title)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_page'] = True
        return context


class PostDeleteView(IsStaffUserMixin, PageTitleMixin, DeleteView):
    model = models.Post
    success_url = reverse_lazy('blog:post_list')

    def get(self, request, *args, **kwargs):
        raise Http404

    def get_object(self, queryset=None):
        post = super().get_object()
        if not post.author == self.request.user:
            raise Http404
        return post
