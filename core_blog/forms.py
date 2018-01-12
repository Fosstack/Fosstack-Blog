from django import forms

from . import models


class CreatePostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = models.Post
        fields = ['content', 'description', 'title', 'slug']
