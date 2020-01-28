from django.forms import ModelForm
from .models import Comment
from django.forms import HiddenInput


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'user', 'text','article')
