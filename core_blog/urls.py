from django.urls import path, register_converter

from . import views, path_converters

app_name = 'blog'

register_converter(path_converters.Hierarchy, 'hierarchy')


urlpatterns = [
    path('', views.ListPostView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('tag/<slug:tag>/', views.ListPostView.as_view(), name="tag"),

    path('category/<hierarchy:hierarchy>/',
         views.CategoryDetailView.as_view(), name='category'),

    path('create/', views.CreatePostView.as_view(), name='post_create'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),

    path(
        '<slug:slug>/edit/', views.PostUpdateView.as_view(), name='post_update'
    ),
    path(
        '<slug:slug>/delete/', views.PostDeleteView.as_view(),
        name='post_delete'
    ),
]
