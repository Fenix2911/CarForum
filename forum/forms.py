from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ["username", "password"]
