from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self) -> str:
        return str(self.product_name)
    
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_on = models.DateTimeField()

class ProductInCart(models.Model):
    class Meta:
        unique_together = (('cart', 'product'))
    product_in_cart_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Order(models.Model):
    STATUS_CHOICES = [
        (1, 'Not Packed'),
        (2, 'Ready For Shipment'),
        (3, 'Shipped'),
        (4, 'Delivered')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

