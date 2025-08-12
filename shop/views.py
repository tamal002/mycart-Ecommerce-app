from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'shop/shophome.html')

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
