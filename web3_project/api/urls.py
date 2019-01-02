from django.conf.urls import url
from django.urls import path
from . import views
from api.resources import ProductResource


urlpatterns = [
    path('',ProductResource, name='products')
]
