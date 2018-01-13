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


class ListPostView(ListView):
    model = models.Post
    context_object_name = 'posts'
    template_name = 'core_blog/list_posts.html'


class PostDetailView(DetailView):
    model = models.Post
    context_object_name = 'post'
    template_name = 'core_blog/post_detail.html'


class CreatePostView(CreateView):
    form_class = forms.CreatePostForm
    success_url = '/'
    template_name = 'core_blog/post_form.html'


class AboutView(TemplateView):
    template_name = 'core_blog/about.html'


class PostUpdateView(UpdateView):
    model = models.Post
    fields = '__all__'
    context_object_name = 'post'
    template_name = 'core_blog/post_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_page'] = True
        return context


class PostDeleteView(DeleteView):
    model = models.Post
    success_url = reverse_lazy('post_list')

    def get_object(self, queryset=None):
        post = super().get_object()
        if not post.author == self.request.user:
            raise Http404
        return post
