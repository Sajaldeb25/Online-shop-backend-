from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Category, Product, CartItem


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', ]


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password', ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    product_category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateSerializer(ProductSerializer):
    product_category = serializers.CharField()

    def create(self, validated_data):
        validated_data['product_category'] = Category.objects.get(id=validated_data['product_category'])
        category_detail = super().create(validated_data)
        return category_detail


class CartItemSerializer(serializers.ModelSerializer):
    ordered_product = ProductCreateSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = '__all__'


class CartItemCreateSerializer(CartItemSerializer):
    ordered_product = serializers.CharField()

    def create(self, validated_data):
        validated_data['ordered_product'] = Product.objects.get(id=validated_data['ordered_product'])
        product_detail = super().create(validated_data)
        return product_detail


