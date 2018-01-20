from django import forms

from tinymce import TinyMCE

from . import models


class DateInput(forms.DateInput):
    input_type = 'date'


class PostForm(forms.ModelForm):

    content = forms.CharField(
        widget=TinyMCE(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = models.Post
        fields = '__all__'
        exclude = ['author', 'read_time', 'hits']
        widgets = {'publish': DateInput()}
