from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.core.files.uploadedfile import InMemoryUploadedFile
from . import forms
import sys
import logging

logger = logging.getLogger(__name__)


class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy("shop:home")
    template_name = "accounts/login.html"

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request, form.get_user())

        return super().form_valid(form)


class LogoutView(generic.RedirectView):
    url = reverse_lazy("shop:home")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class SignUp(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


def changeProfile(request):
    from PIL import Image
    import io
    user = request.user
    if request.method == 'POST':

        user_form = forms.UserChangeForm(request.POST, instance=user)
        profile_form = forms.ProfileChangeForm(request.POST, request.FILES, instance=user.profile)

        if all((profile_form.is_valid(), user_form.is_valid())):
            user_form.save()
            profile_form.save()
            username = user.username
            messages.success(request, f'Profile was changed for {username}!')
            return redirect('shop:profile')
    else:
        user_form = forms.UserChangeForm(instance=user)
        profile_form = forms.ProfileChangeForm(instance=user.profile)
    return render(request, 'accounts/change.html', {'profile_form': profile_form, 'user_form': user_form})
