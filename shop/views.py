from django.shortcuts import render
from shop.models import Product
# Create your views here.

def index(request):
    products = Product.objects.all()
    params = {
        'product_list': products,
        'products_per_row': 5,
    }
    return render(request, 'shop/shophome.html', params)

def about_us(request):
    return render(request, 'shop/about.html')

def contact(request):
    pass

def tracker(request):
    pass

def search(request):
    pass

def product_view(request):
    pass

def ckeckout(request):
    pass
