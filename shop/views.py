from django.shortcuts import render, redirect
from shop.models import Product, Enquiry, Cart, CartItem, UserAddress, Order
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    products = Product.objects.all()
    categories = {}
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

@login_required(login_url="accounts:login")
def tracker(request):
    # first time after placing order
    if(request.method == "POST"):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        name = first_name + last_name
        address_1 = request.POST.get("address_1")
        address_2 = request.POST.get("address_2")
        country = request.POST.get("country")
        state = request.POST.get("state")
        zip_code = request.POST.get("zip")
        payment_method = request.POST.get("payment_method")
        if UserAddress.objects.filter(user=request.user).exists():
            pass
        else:
            UserAddress.objects.create(user=request.user, name=name, address_1=address_1, address_2=address_2, country=country, state=state, zip_code=zip_code)
        
        # strore the order details at database
        user_cart = get_user_cart(request.user)
        cart_items = CartItem.objects.filter(cart=user_cart)
        for item in cart_items:
            Order.objects.create(user=request.user, product=item.product, payment_status=payment_method, quantity=item.quantity)
            item.delete()
        
    orders = Order.objects.filter(user=request.user).order_by("-order_time_stamp")
    
    
    return render(request, 'shop/tracker.html', {"orders": orders})

@login_required(login_url="accounts:login")
def cancel_order(request, id):
    item = Order.objects.get(id=id)
    item.delete()
    return redirect("shop:tracker")


def search(request):
    return render(request, 'shop/search.html')

def product_view(request, id):
    # fetching the product details using the product-id
    product = Product.objects.get(product_id=id)
    return render(request, 'shop/productview.html', {"product": product})

@login_required(login_url="accounts:login")
def cart(request):
    return render(request, 'shop/cartView.html')

@login_required(login_url="accounts:login")
def ckeckout(request):
    cart = get_user_cart(request.user)
    item_list = CartItem.objects.filter(cart=cart)
    no_items = len(item_list)
    cart_cost = 0
    for item in item_list:
        cart_cost += item.quantity * item.product.price
    return render(request, 'shop/checkout.html', {"items": item_list, "no_of_items": no_items, "cost": cart_cost})


def get_user_cart(user):
    cart, exists = Cart.objects.get_or_create(user=user)
    return cart

@login_required(login_url="accounts:login")
def add_to_cart(request, id):
    product = Product.objects.get(product_id=id)
    cart = get_user_cart(request.user)

    if CartItem.objects.filter(cart=cart, product_id=id).exists():
        cart_item = CartItem.objects.get(cart=cart, product_id=id)
        cart_item.quantity += 1
        cart_item.save()
    else:
        CartItem.objects.create(cart=cart, product=product)
    
    return redirect("shop:product_view", id=product.product_id)
        
@login_required(login_url="accounts:login")
def remove_from_cart(request, id):
    cart = get_user_cart(request.user)
    cart_item = CartItem.objects.get(cart=cart, product_id=id)
    cart_item.quantity -= 1
    if cart_item.quantity <= 0:
        cart_item.delete()
    else:
        cart_item.save()
    return redirect("shop:loadcart")

@login_required(login_url="accounts:login")
def cart_details(request):
    cart = get_user_cart(request.user)
    item_list = CartItem.objects.filter(cart=cart)
    return render(request, "shop/cartView.html", {"items": item_list})