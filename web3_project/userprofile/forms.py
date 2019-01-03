from django.contrib.auth.forms import AuthenticationForm
from django_registration.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username']


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'description', 'quote', 'image']