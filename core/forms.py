from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'content', 'cover_image', 'category', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-4 text-xl font-bold border-b border-gray-200 focus:outline-none focus:border-blue-500 placeholder-gray-400',
                'placeholder': 'Enter an amazing title...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full h-screen p-6 text-lg font-mono text-gray-700 focus:outline-none resize-none',
                'placeholder': 'Start writing your story...'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full p-2 bg-white border border-gray-300 rounded shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'status': forms.Select(attrs={
                'class': 'w-full p-2 bg-white border border-gray-300 rounded shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            # File input is handled automatically by Django, but we can style it in the template
        }