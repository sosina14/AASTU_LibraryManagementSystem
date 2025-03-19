from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

from .models import Book

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=[('student', 'Student')], widget=forms.HiddenInput())

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'description', 'available_copies']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
