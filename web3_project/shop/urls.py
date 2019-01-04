from django.conf.urls import url
from django.urls import path
from .views import ProductListView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('cart/', views.cart, name='cart'),
    path('<category_slug>/', ProductListView.as_view(), name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    
]
