from django.contrib.auth import login, logout, get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.sites.shortcuts import get_current_site
from django.core import signing
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django_registration import signals
from django_registration.exceptions import ActivationError
from django_registration.views import ActivationView as BaseActivationView
from django_registration.views import RegistrationView as BaseRegistrationView
from . import forms
import sys

import logging

logger = logging.getLogger(__name__)

REGISTRATION_SALT = getattr(settings,'REGISTRATION_SALT', 'registration')

class RegistrationView(BaseRegistrationView):
    email_body_template = 'django_registration/activation_email_body.txt'
    email_subject_template = 'django_registration/activation_email_subject.txt'
    success_url = reverse_lazy('registration_complete')
    


    def register(self, form):
        new_user = self.create_inactive_user(form)
        signals.user_registered.send(
            sender=self.__class__,
            user=new_user,
            request=self.request
        )
        messages.success(self.request,f'Registration completed {new_user}, check your email!')
        return new_user
       

    def create_inactive_user(self,form):
        new_user = form.save(commit=True)
        new_user.is_active = False
        new_user.save()

        self.send_activation_email(new_user)
        return new_user

    def get_activation_key(self,user):
        return signing.dumps(
            obj=user.get_username(),
            salt=REGISTRATION_SALT
        )

    def get_email_context(self, activation_key):
        scheme = 'https' if self.request.is_secure() else 'http'
        return {
            'scheme': scheme,
            'activation_key': activation_key,
            'expiration_days':settings.ACCOUNT_ACTIVATION_DAYS,
            'site': get_current_site(self.request)
        }

    def send_activation_email(self, user):
        activation_key = self.get_activation_key(user)
        context = self.get_email_context(activation_key)
        context['user'] = user
        subject = render_to_string(
            template_name=self.email_subject_template,
            context=context,
            request=self.request
        )
        # Force subject to a single line to avoid header-injection

        subject = ''.join(subject.splitlines())
        message = render_to_string(
            template_name=self.email_body_template,
            context=context,
            request=self.request
        )
        user.email_user(subject,message + activation_key, settings.DEFAULT_FROM_EMAIL)

        

class ActivationView(BaseActivationView):
    ALREADY_ACTIVATED_MESSAGE = _(
        u'The account you tried to activate has already been activated.'
    )

    BAD_USERNAME_MESSAGE= _(
        u'The account you attempted to activate is invalid'
    )

    EXPIRED_MESSAGE = _(u'This account has expired.')
    INVALID_KEY_MESSAGE = _(
        u'The activation key you provided is invalid.'
    )

    success_url = reverse_lazy('activation_complete')

    def activate(self, *args, **kwargs):
        username = self.validate_key(kwargs.get('activation_key'))
        user = self.get_user(username)
        user.is_active = True
        user.save()
        messages.success(self.request,f'account activated, you may now log in')

        return user

    def validate_key(self,activation_key):
        try:
            username = signing.loads(
                activation_key,
                salt=REGISTRATION_SALT,
                max_age=settings.ACCOUNT_ACTIVATION_DAYS* 86400
            )
            return username
        except signing.SignatureExpired:
            raise ActivationError(self.EXPIRED_MESSAGE, code='expired')
            messages.warning(self.request,f'seems like your activation code has expired!')
        except signing.BadSignature:
            raise ActivationError(self.INVALID_KEY_MESSAGE, code='invalid_key', params={'activation_key' : activation_key})

    def get_user(self,username):
            User = get_user_model()
            try:
                user = User.objects.get(**{User.USERNAME_FIELD: username,})
                if user.is_active:
                    raise ActivationError(
                        self.ALREADY_ACTIVATED_MESSAGE,code='already_activated'
                    )
                return user
            except User.DoesNotExist:
                raise ActivationError(
                    self.BAD_USERNAME_MESSAGE,
                    code='bad_username'
                )



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




# def changeProfile(request):
#     from PIL import Image
#     import io
#     user = request.user
#     if request.method == 'POST':

#         user_form = forms.UserChangeForm(request.POST, instance=user)
#         profile_form = forms.ProfileChangeForm(request.POST, request.FILES, instance=user.profile)

#         if all((profile_form.is_valid(), user_form.is_valid())):
#             user_form.save()
#             profile_form.save()
#             username = user.username
#             messages.success(request, f'Profile was changed for {username}!')
#             return redirect('shop:profile')
#     else:
#         user_form = forms.UserChangeForm(instance=user)
#         profile_form = forms.ProfileChangeForm(instance=user.profile)
#     return render(request, 'accounts/change.html', {'profile_form': profile_form, 'user_form': user_form})
