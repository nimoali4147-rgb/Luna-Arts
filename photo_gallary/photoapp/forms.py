from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'w-full rounded-lg border-2 border-gray-300 p-3', 
            'placeholder': 'Enter your email'
        })
    ) 

    class Meta:
        model = User
        field = ['username', 'email', 'password' ]

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                'An account with this email already exists.'
            )

        return email