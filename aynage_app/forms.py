from django import forms
from .models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'category', 'description', 'status', 'banner']

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = [
            'title', 'department', 'experience', 'job_type', 'description',
            'location', 'salary', 'banner', 'status', 'deadline'
        ]