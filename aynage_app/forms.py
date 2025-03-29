from django import forms
from .models import *

class BlogForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True    
    )

    class Meta:
        model = Blog
        fields = ['title', 'categories', 'description', 'status', 'banner']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'rich-text-editor'}),
        }


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = [
            'title', 'department', 'experience', 'job_type', 'description',
            'location', 'salary', 'banner', 'status', 'deadline'
        ]