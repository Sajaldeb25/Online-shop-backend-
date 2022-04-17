import os.path

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    def filenamechange(instance, filename):
        upload_to = "product_images"
        exten = filename.split('.')[-1]  # find extension
        # print(instance.product_name)
        # print(instance.product_price)
        # print(instance.product_category)
        filename = '{}_{}.{}'.format(instance.product_name, instance.product_category, exten)
        return os.path.join(upload_to, filename)

    product_name = models.CharField(max_length=30)
    product_description = models.CharField(max_length=200)
    product_price = models.IntegerField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_picture = models.ImageField(upload_to=filenamechange, blank=True)


class CartItem(models.Model):
    carted_by_customer = models.ForeignKey(User, on_delete=models.CASCADE)  # customer details
    carted_product = models.ForeignKey(Product, on_delete=models.CASCADE)  # product details
    quantity = models.IntegerField()  # number
    order_flag = models.BooleanField(default=False)


class Order(models.Model):
    ordered_by_customer = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_product = models.ForeignKey(CartItem, on_delete=models.CASCADE)


