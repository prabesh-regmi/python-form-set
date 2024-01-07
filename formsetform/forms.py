# forms.py

from django import forms
from django.forms import inlineformset_factory
from .models import Author, Book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form form-control text-input','placeholder': 'Enter the Author name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter the Author email','class': 'form form-control text-input'}),
        }
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publication_date']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter the book title','class': 'form form-control text-input'}),
            'publication_date': forms.DateInput(attrs={'type': 'date','class': 'form form-control'}),
        }

BookFormSet = inlineformset_factory(Author, Book, form=BookForm,can_delete=False, extra=1)
