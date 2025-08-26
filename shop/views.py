from django.shortcuts import render
from shop.models import Product
# Create your views here.

def index(request):
    products = Product.objects.all()
    categories = {};
    for product in products:
        if product.category not in categories:
            categories[product.category] = []
        categories[product.category].append(product)
    context = {
        'category_list': categories 
    }
    return render(request, 'shop/shophome.html', context)

def about_us(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def product_view(request, id):
    # fetching the product details using the product-id
    product = Product.objects.get(product_id=id)
    return render(request, 'shop/productview.html', {"product": product})

def ckeckout(request):
    return render(request, 'shop/checkout.html')
