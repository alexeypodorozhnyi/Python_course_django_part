from django.forms import ModelForm,Form
from .models import Note,Profile
from django import forms

class NoteForm(ModelForm):

    class Meta:
        model = Note
        fields = ('name','text')


class UpdateNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['is_shared', ]


class ConfirmEmailForm(forms.Form):
    email_confirm = forms.CharField()

