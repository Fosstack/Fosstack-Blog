from django.urls import path

from . import views

app_name = 'back_office'

urlpatterns = [
    path('contact', views.CreateContactView.as_view(), name='contact'),
]
