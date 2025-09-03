from django.shortcuts import render, redirect
from shop.models import Product, Enquiry, Cart, CartItem
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
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("number")
        query = request.POST.get("message")
        new_qnuery = Enquiry.objects.create(name=name, email=email, phone=phone, query=query)
        return redirect('shop:contact')
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def product_view(request, id):
    # fetching the product details using the product-id
    product = Product.objects.get(product_id=id)
    return render(request, 'shop/productview.html', {"product": product})

def cart(request):
    return render(request, 'shop/cartView.html')


def ckeckout(request):
    return render(request, 'shop/checkout.html')


def get_user_cart(user):
    cart, exists = Cart.objects.get_or_create(user=user)
    return cart


def add_to_cart(request, id):
    product = Product.objects.get(product_id=id)
    cart = get_user_cart(request.user)

    if CartItem.objects.filter(cart=cart, product_id=id).exists():
        cart_item = CartItem.objects.get(cart=cart, product_id=id)
        cart_item.quantity += 1
        cart_item.save()
    else:
        CartItem.objects.create(cart=cart, product=product)

    return render(request, 'shop/productview.html', {"product": product})
        

def remove_from_cart(request, id):
    cart = get_user_cart(request.user)
    cart_item = CartItem.objects.get(cart=cart, product_id=id)
    context = {"items":{}}
    cart_item.quantity -= 1
    if cart_item.quantity <= 0:
        cart_item.delete()
    else:
        cart_item.save()
    context["items"] = CartItem.objects.filter(cart=cart)
    return render(request, 'shop/cartView.html', context)


def cart_details(request):
    cart = get_user_cart(request.user)
    item_list = CartItem.objects.filter(cart=cart)
    return render(request, "shop/cartView.html", {"items": item_list})