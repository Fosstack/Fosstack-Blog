from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView

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


class CreatePost(CreateView):
    form_class = forms.CreatePostForm
    success_url = '/'
    template_name = 'core_blog/post_form.html'


class AboutView(TemplateView):
    template_name = 'core_blog/about.html'
