from django.db.models import F, Q
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404

from . import forms
from . import models
from .mixins import IsStaffUserMixin, PageTitleMixin


class ListPostView(ListView):
    model = models.Post
    context_object_name = 'posts'
    paginate_by = 7

    def get_queryset(self):
        if self.request.user.is_authenticated:
            result = self.model.objects.annotate(
                writer=F('author__first_name'))
        else:
            result = self.model.objects.active().annotate(
                writer=F('author__first_name'))

        # search filter
        query = self.request.GET.get('q')
        if query:
            result = result.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(writer__icontains=query))

        # filter by tag
        if 'tag' in self.kwargs:
            tag = self.kwargs['tag']
            result = result.filter(tags__name__in=[tag])

        return result


class ListTipView(ListView):
    model = models.Post
    context_object_name = 'posts'
    paginate_by = 7

    def get_queryset(self):
        if self.request.user.is_authenticated:
            result = self.model.objects.annotate(
                writer=F('author__first_name')).filter(post_type='tip')
        else:
            result = self.model.objects.active().annotate(
                writer=F('author__first_name')).filter(post_type='tip')
        return result


class CategoryDetailView(PageTitleMixin, DetailView):
    model = models.Category
    context_object_name = 'category'
    page_title = ""

    def get_object(self):
        category_slug = self.kwargs['hierarchy'].split('/')
        parent = None
        root = self.model.objects.prefetch_related('post_set').all()
        for slug in category_slug:
            parent = get_object_or_404(root, slug=slug, parent=parent)
        self.page_title = str(parent).capitalize()
        return parent


class PostDetailView(PageTitleMixin, DetailView):
    model = models.Post
    context_object_name = 'post'
    page_title = ''
    post = None

    def get_object(self, queryset=None):
        slug = self.kwargs['slug']
        try:
            post = self.model.objects.select_related('author').get(slug=slug)
            if (not post.is_published
                    and not self.request.user.is_authenticated):
                raise Http404
        except self.model.DoesNotExist:
            raise Http404
        self.page_title = post.title
        self.post = post
        return post

    def get_context_data(self, **kwargs):
        session_key = f'viewed_post_{self.post.pk}'
        if not self.request.session.get(session_key, False):
            self.post.view_count = F('view_count') + 1
            self.post.save()
            self.post.refresh_from_db()
            self.request.session[session_key] = True
        return super().get_context_data(**kwargs)


class CreatePostView(IsStaffUserMixin, PageTitleMixin, CreateView):
    form_class = forms.PostForm
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
        if (request.user.is_superuser
                or request.user == self.get_object().author):
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
