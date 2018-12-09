from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from accounts.models import Profile
from django.contrib.auth import get_user_model


# Create your views here.


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/products.html', {'category': category,
                                                  'categories': categories,
                                                  'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    if request.method == 'POST':
        cart_product_form = CartAddProductForm(request.POST)
    else:
        cart_product_form = CartAddProductForm()

    return render(request, 'shop/detail.html', {'product': product, 'cart_product_form': cart_product_form})


def home(request):
    return render(request, 'shop/home.html')


def cart(request):
    return render(request, 'shop/cart.html')


def profile(request):
    user = request.user
    return render(request, 'shop/profile.html', {'profile': user.profile})
