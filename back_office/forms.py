from django import forms
from .models import Contact ,Subscribe


class contact_form(forms.ModelForm):
    class Meta:
        model = Contact

    fields = '__all__'
