from django import forms
from webapp.models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        exclude = ('word', 'timestamp',)
