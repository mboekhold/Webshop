from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.profile, name='profile'),
    path('change/', views.changeProfile, name='change_profile'),

]
