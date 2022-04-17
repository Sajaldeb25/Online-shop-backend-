# Generated by Django 4.0.3 on 2022-04-17 13:21

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_product_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_picture',
            field=models.ImageField(blank=True, upload_to=shop.models.Product.filenamechange),
        ),
    ]
