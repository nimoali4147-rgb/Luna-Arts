from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        input_class = (
            'w-full rounded-lg border border-gray-300 '
            'bg-stone-50 px-4 py-3 text-sm text-stone-900 '
            'outline-none transition '
            'focus:border-amber-600 focus:ring-2 '
            'focus:ring-amber-100'
        )

        placeholders = {
            'username': 'Choose a username',
            'email': 'Enter your email address',
            'password1': 'Create a password',
            'password2': 'Confirm your password',
        }

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': input_class,
                'placeholder': placeholders.get(name, ''),
            })

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                'An account with this email already exists.'
            )

        return email


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': (
                    'w-full rounded-xl border border-stone-200 '
                    'bg-stone-50 px-4 py-3.5 text-sm text-stone-900 '
                    'transition duration-200 '
                    'placeholder:text-stone-400 '
                    'hover:border-stone-300 '
                    'focus:border-amber-600 focus:bg-white '
                    'focus:outline-none focus:ring-4 focus:ring-amber-100'
                ),
            }),
            'email': forms.EmailInput(attrs={
                'class': (
                    'w-full rounded-xl border border-stone-200 '
                    'bg-stone-50 px-4 py-3.5 text-sm text-stone-900 '
                    'transition duration-200 '
                    'placeholder:text-stone-400 '
                    'hover:border-stone-300 '
                    'focus:border-amber-600 focus:bg-white '
                    'focus:outline-none focus:ring-4 focus:ring-amber-100'
                ),
            }),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio']
        widgets = {
            'bio': forms.Textarea(attrs={
                'rows': 4,
                'maxlength': 500,
                'placeholder': 'Tell us a little about yourself...',
                'class': (
                    'w-full rounded-xl border border-stone-200 '
                    'bg-stone-50 px-4 py-3 text-sm text-stone-900 '
                    'focus:border-amber-600 focus:outline-none '
                    'focus:ring-4 focus:ring-amber-100'
                ),
            }),
        }
