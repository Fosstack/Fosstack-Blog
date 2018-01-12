from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.HomeView.as_view(), name='home'),
    re_path(r'^create/$', views.CreatePost.as_view(), name='create_post')
]
