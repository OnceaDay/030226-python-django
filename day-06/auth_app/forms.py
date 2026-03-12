from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile

User = get_user_model()


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={"placeholder": "Choose a username"}
        ),
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder": "Enter your email"}
        ),
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Create a password"}
        ),
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirm your password"}
        ),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter username"}
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter password"}
        ),
    )


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["bio", "age", "location", "profile_photo"]
        widgets = {
            "bio": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Tell people a little about yourself and your mission...",
                }
            ),
            "age": forms.NumberInput(
                attrs={
                    "placeholder": "Enter your age",
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "placeholder": "Enter your location",
                }
            ),
        }