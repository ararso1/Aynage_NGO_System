from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['category', 'title', 'author', 'description', 'banner', 'status']