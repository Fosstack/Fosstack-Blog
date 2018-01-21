from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.urls import reverse
from datetime import date

from taggit.managers import TaggableManager
from tinymce import HTMLField
from mptt.models import MPTTModel, TreeForeignKey

from .utils import get_read_time


class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super().filter(draft=False).filter(publish__lte=date.today())


class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=250, blank=True, null=True)
    category = TreeForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
        )
    content = HTMLField('Content')
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    publish = models.DateField(auto_now=False, auto_now_add=False,)
    read_time = models.IntegerField(default=0)
    hits = models.IntegerField(default=0)
    draft = models.BooleanField(default=True)
    author = models.ForeignKey(
            settings.AUTH_USER_MODEL, default=1,
            on_delete=models.SET_DEFAULT
        )
    tags = TaggableManager()
    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    @property
    def in_future(self):
        return (self.publish > date.today()) and not self.draft

    class Meta:
        ordering = ['-publish']


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        'self', null=True, blank=True, related_name='children',
        db_index=True, on_delete=models.CASCADE
        )
    slug = models.SlugField()

    class Meta:
        unique_together = (('parent', 'slug',))
        verbose_name_plural = 'Categories'

    def get_slug_list(self):
        try:
            ancestors = self.get_ancestors(include_self=True)
        except Exception:
            ancestors = []
        else:
            ancestors = [i.slug for i in ancestors]
        slug_string = []
        for i in range(len(ancestors)):
            slug_string.append('/'.join(ancestors[:i+1]))
        return slug_string

    def get_absolute_url(self):
        return reverse(
            "blog:category", kwargs={'hierarchy': self.get_slug_list()[-1]})

    def __str__(self):
        return self.name


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if instance.content:
        instance.read_time = get_read_time(instance.content)


pre_save.connect(pre_save_post_receiver, sender=Post)
