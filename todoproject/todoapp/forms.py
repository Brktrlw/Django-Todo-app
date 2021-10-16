from django import forms
from .models import Todo

class TodoForm(forms.Form):
    title = forms.CharField(label='title', max_length=100)
    description = forms.CharField(label='description')

