from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget

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
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Vacancy
        fields = [
            'title', 'department', 'experience', 'job_type', 'description',
            'location', 'salary', 'banner', 'status', 'deadline'
        ]