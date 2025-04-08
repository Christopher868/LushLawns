from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms
from .models import Info

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


class InfoForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name'}), help_text="Required. Must be 30 characters or less", max_length=30)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name'}), help_text="Required. Must be 30 characters or less", max_length=30)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email address'}), help_text="Required.")
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone number'}), help_text="Required.", max_length=15)
    street = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Street address'}), help_text="Required.", max_length=50)
    state = forms.ChoiceField(choices=[('', 'Select a state')] + list(Info.STATE_CHOICES), widget=forms.Select(attrs={'class': 'form-control'}))
    zipcode = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Zipcode'}), help_text="Required.", max_length=9)
    card = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Card Number'}), help_text="Required.", max_digits=16)
    security_code = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Security Code'}), help_text="Required.", max_digits=3)
    expiration = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Card expiration date'}), help_text="Format DD/YY", max_length=5)

    class Meta:
        model = Info
        fields = [
        'first_name', 'last_name', 'email',
        'phone_number', 'street', 'state',
        'zipcode', 'card', 'security_code', 'expiration'
    ]
        

class EditUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']