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
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter seller email',
            }),
            'profile_picture': forms.ClearableFileInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        input_class = "w-full px-4 py-2 border border-gray-300 rounded-md bg-gray-50 focus:outline-none focus:ring-2 focus:ring-purple-500"

        # Apply Tailwind styling to ALL fields
        self.fields['username'].widget.attrs.update({'class': input_class})
        self.fields['email'].widget.attrs.update({'class': input_class})
        self.fields['password1'].widget.attrs.update({'class': input_class})
        self.fields['password2'].widget.attrs.update({'class': input_class})

        self.fields['profile_picture'].widget.attrs.update({
            'class': 'w-full text-sm text-gray-600'
        })