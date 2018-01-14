from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.ListPostView.as_view(), name='post_list'),
    path('about', views.AboutView.as_view(), name='about'),
    path('create', views.CreatePostView.as_view(), name='post_create'),
    path('<slug:slug>', views.PostDetailView.as_view(), name='post_detail'),

    path(
        '<slug:slug>/edit', views.PostUpdateView.as_view(), name='post_update'
    ),
    path(
        '<slug:slug>/delete', views.PostDeleteView.as_view(),
        name='post_delete'
    ),
]
