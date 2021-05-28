from django import forms
from .models import Blog

class BlogForms(forms.ModelForm):
    model = Blog
    fields = '__all__'