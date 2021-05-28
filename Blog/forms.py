from django import forms
from .models import Blog

class BlogForms(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

    
    #def clean(self):
        #cleaned_data=super().clean()
        #title = cleaned_data.get('title')
        #description= cleaned_data.get('description')