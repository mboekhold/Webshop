from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views as account_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('mydata/', account_views.generate_pdf, name='mydata'),
    path('activate/complete/',
        TemplateView.as_view(
            template_name='django_registration/activation_complete.html'
        ),
        name='activation_complete'),
    # The activation key can make use of any character from the
    # URL-safe base64 alphabet, plus the colon as a separator.
    url(r'^activate/(?P<activation_key>[-:\w]+)/$',
        account_views.ActivationView.as_view(),
        name='registration_activate'),
    url(r'^register/$',
        account_views.RegistrationView.as_view(),
        name='registration_register'),
    url(r'^register/complete/$',
        TemplateView.as_view(
            template_name='django_registration/registration_complete.html'
        ),
        name='registration_complete'),
    url(r'^register/closed/$',
        TemplateView.as_view(
            template_name='django_registration/registration_closed.html'
        ),
        name='registration_disallowed'),

]
