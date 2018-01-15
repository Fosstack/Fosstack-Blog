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
from .mixins import IsStaffUserMixin, PageTitleMixin


class ListPostView(ListView):
    model = models.Post
    context_object_name = 'posts'
    paginate_by = 7
    template_name = 'core_blog/list_posts.html'

    def get_queryset(self):
        return self.model.objects.select_related('author').all()


class PostDetailView(PageTitleMixin, DetailView):
    model = models.Post
    context_object_name = 'post'
    page_title = ''
    template_name = 'core_blog/post_detail.html'

    def get_object(self, queryset=None):
        slug = self.kwargs['slug']
        try:
            post = self.model.objects.values(
                'title', 'description', 'publish', 'draft',
                'author__username', 'content', 'slug'
                ).get(slug=slug)
        except self.model.DoesNotExist:
            raise Http404
        self.page_title = post['title']
        return post


class CreatePostView(IsStaffUserMixin, PageTitleMixin, CreateView):
    form_class = forms.PostForm
    success_url = '/'
    page_title = 'Create Awesome Post'
    template_name = 'core_blog/post_form.html'


class AboutView(PageTitleMixin, TemplateView):
    page_title = 'About'
    template_name = 'core_blog/about.html'


class PostUpdateView(IsStaffUserMixin, PageTitleMixin, UpdateView):
    form_class = forms.PostForm
    model = models.Post
    context_object_name = 'post'
    template_name = 'core_blog/post_form.html'

    def get(self, request, *args, **kwargs):
        if (
            request.user.is_superuser or
            request.user == self.get_object().author
        ):
            return super().get(request, *args, **kwargs)
        raise Http404

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
