from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views as profile_views

urlpatterns = [
    path('', profile_views.changeProfile, name='profile'), 
]
