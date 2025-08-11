from django.db import models

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

