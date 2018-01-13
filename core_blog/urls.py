from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.ListPostView.as_view(), name='list_post'),
    re_path(r'^create/$', views.CreatePost.as_view(), name='create_post'),
    re_path(r'^about/$', views.AboutView.as_view(), name='about'),
    path(
        '<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'
    ),
]
