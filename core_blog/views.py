from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from . import models


class HomeView(TemplateView):
    template_name = "core_blog/index.html"


class CreatePost(CreateView):
    model = models.Post
    fields = '__all__'
    template_name = 'core_blog/create_post.html'
