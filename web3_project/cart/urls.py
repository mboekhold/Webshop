from django.conf.urls import url
from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    # url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    # url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
]
