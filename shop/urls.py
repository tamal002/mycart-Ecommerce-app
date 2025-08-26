
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('tracker/', views.tracker, name='tracker'),
    path('search/', views.search, name='search'),
    path('productview/<int:id>/', views.product_view, name='product_view'),
    path('ckeckout/', views.ckeckout, name='ckeckout'),
]
