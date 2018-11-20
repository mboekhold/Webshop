from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.part_list),
]