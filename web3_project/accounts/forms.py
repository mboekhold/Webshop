from django.contrib.auth.forms import AuthenticationForm
from django_registration.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = User

