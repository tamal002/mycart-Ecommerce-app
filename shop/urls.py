
from django.urls import path, include
from . import views

app_name = "shop"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('tracker/', views.tracker, name='tracker'),
    path('search/', views.search, name='search'),
    path('productview/<int:id>/', views.product_view, name='product_view'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.ckeckout, name='checkout'),
    path('addtocart/<int:id>/', views.add_to_cart, name='addtocart'),
    path('removecart/<int:id>/', views.remove_from_cart, name='removecart'),
    path('loadcart/', views.cart_details, name='loadcart'),
]
