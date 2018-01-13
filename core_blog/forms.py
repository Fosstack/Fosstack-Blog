from django import forms
from tinymce import TinyMCE
from . import models


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class CreatePostForm(forms.ModelForm):
	content = forms.CharField(widget=TinyMCEWidget(
	attrs={'required': False,
	'cols': 30,
	'rows': 10}))

	class Meta:
		model = models.Post
		fields = ['content', 'description', 'title', 'slug']
