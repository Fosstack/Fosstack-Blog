from django import forms

from tinymce import TinyMCE

from . import models


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class DateInput(forms.DateInput):
    input_type = 'date'


class PostForm(forms.ModelForm):

    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = models.Post
        fields = '__all__'
        exclude = ['author', 'read_time', 'hits']
        widgets = {'publish': DateInput()}
