from django.shortcuts import render


def home(request):
    return render(request, 'shop/home.html')

def products(request):
    return render(request, 'shop/products.html')

