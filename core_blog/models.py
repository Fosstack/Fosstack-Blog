from django.db import models
from django.conf import settings
from tinymce import HTMLField


class Post(models.Model):
    content = HTMLField('Content')
    description = models.TextField(max_length=250, blank=True, null=True)
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    draft = models.BooleanField(default=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=1,
        on_delete=models.SET_DEFAULT
        )

    def __str__(self):
        return self.title
