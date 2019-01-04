from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.views.generic import ListView


# Create your views here.

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['category'] = None
        return context

    def get_queryset(self):
        if self.kwargs.get('category_slug'):
            category_slug = self.kwargs.get('category_slug')
            category = get_object_or_404(Category, slug=category_slug)
            return Product.objects.filter(category=category, available=True)
        return Product.objects.filter(available=True)


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
