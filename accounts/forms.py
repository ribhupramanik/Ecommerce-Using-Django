from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'profile_picture']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            'profile_picture': forms.ClearableFileInput()
        }

class SellerRegistrationForm(UserCreationForm):
    class Meta: 
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'profile_picture']

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Enter seller username', 
                'class': 'form-input'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter seller email', 
                'class': 'form-input'
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'form-input'
            })
        }