from django.views.generic.edit import CreateView
from . import forms


class CreateContactView(CreateView):
    form_class = forms.ContactForm
    success_url = '/'
    template_name = 'back_office/contact.html'
