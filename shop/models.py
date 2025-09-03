from django.db import models
from django.conf import settings

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='shop/images', default="")
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    description = models.TextField()
    price = models.IntegerField(default=0)
    launched_date = models.DateField()

    def __str__(self):
        return self.product_name
    

class Enquiry(models.Model):
    enq_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    query = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    

class CartItem(models.Model):
    cart = models.ForeignKey("Cart", related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity =  models.IntegerField(default=1)

    def __str__(self):
        return self.cart.user.username
