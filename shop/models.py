from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=30)
    product_description = models.CharField(max_length=200)
    product_price = models.IntegerField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class CartItem(models.Model):
    order_by_customer = models.ForeignKey(User, on_delete=models.CASCADE)  # customer details
    ordered_product = models.ForeignKey(Product, on_delete=models.CASCADE)  # product details
    quantity = models.IntegerField()  # number
    total_cost = models.IntegerField()  # per piece cost * quantity
