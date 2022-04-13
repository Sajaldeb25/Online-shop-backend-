from django.db import models


# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name


class Products(models.Model):
    product_name = models.CharField(max_length=30)
    product_description = models.CharField(max_length=200)
    product_price = models.IntegerField()
    product_category = models.ForeignKey(Categories, on_delete=models.CASCADE)

