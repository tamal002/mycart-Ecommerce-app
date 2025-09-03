from django.contrib import admin
from .models import Product, Enquiry, Cart, CartItem

admin.site.register(Product)
admin.site.register(Enquiry)
admin.site.register(Cart)
admin.site.register(CartItem)
