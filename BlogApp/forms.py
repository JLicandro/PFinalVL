from django import forms
from .models import BlogModel


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = BlogModel
        fields = ('imagen')