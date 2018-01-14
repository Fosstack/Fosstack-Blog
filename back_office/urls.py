from django.urls import re_path
from django.views.generic import TemplateView
from . import views

app_name = 'back_office'

urlpatterns = [
    re_path(r'^contact/', views.CreateContactView.as_view()),
    re_path(r'^about/', TemplateView.as_view(template_name='back_office/about.html')),
]
