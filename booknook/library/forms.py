# booknook/library/forms.py
from django import forms
from .models import Tag

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Fantasy', 'maxlength': 40})
        }
        labels = {
            'name': 'Tag name',
        }
0