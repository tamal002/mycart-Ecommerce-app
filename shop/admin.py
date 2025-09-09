from django.contrib import admin
from .models import Product, Enquiry, Cart, CartItem, Order, UserAddress

admin.site.register(Product)
admin.site.register(Enquiry)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(UserAddress)
admin.site.register(Order)
