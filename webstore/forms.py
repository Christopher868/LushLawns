from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'}), help_text="Required. Must be 30 characters or less", max_length=30)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}), help_text="Required. Must be 30 characters or less", max_length=30)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter a valid email address'}), help_text="Required.")
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter a username'}), help_text="Required. Must be 30 characters or less", max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter a Password'}), help_text="Required. Must be between 8-20 characters", max_length=20, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}), help_text="Required. Must match password", max_length=20, label="Confirm Password")
    
    class meta:
        model= User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']