from django.contrib.auth.models import User
from django.db.models import F
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from shop.serializers import RegisterSerializer, LoginSerializer, ProductSerializer, ProductCreateSerializer, \
    CategorySerializer, CartItemSerializer, CartItemCreateSerializer, OrderItemSerializer, OrderItemCreateSerializer
from .models import Category, Product, CartItem


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username=username).first()
        if user is None:
            raise AuthenticationFailed('User does not exist.')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password.')
        # jwt : https://www.youtube.com/watch?v=PUzgZrS_piQ&list=LL&index=18&t=1150s     (after 22 min)
        # not needed initially (13 april, 2022)

        return Response(data='Valid user.')
        # print(password, user)


class CategoryView(APIView):
    def get(self, request):  # to see categories
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):  # to create categories
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ProductCreateSerializer(data=request.data)

        try:
            if Category.objects.get(id=request.data['product_category']):
                if serializer.is_valid():
                    serializer.save()
                    details_serializer = ProductSerializer(instance=serializer.instance)
                    return Response(details_serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            res = {'msg': 'Category does not exists.'}
            return Response(res)


class CartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart_item = CartItem.objects.filter(carted_by_customer=request.user.id)
        serializer = CartItemSerializer(cart_item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        request.data['carted_by_customer'] = request.user.id
        serializer = CartItemCreateSerializer(data=request.data)

        try:
            if Product.objects.get(id=request.data['carted_product']):
                if serializer.is_valid():
                    serializer.save()
                    detail_serializer = CartItemSerializer(instance=serializer.instance)
                    return Response(detail_serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            res = {'msg': 'Product does not exists.'}
            return Response(res)


class UserOrderedItemView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        ordered_by_user = CartItem.objects.filter(carted_by_customer=request.user.id, order_flag=True)
        serializer = CartItemSerializer(ordered_by_user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        CartItem.objects.filter(carted_by_customer=request.user.id, order_flag=False)\
            .update(order_flag=True)
        return Response(status=status.HTTP_200_OK)


class BlacklistRefreshView(APIView):
    def post(self, request):
        token = RefreshToken(request.data.get('refresh'))
        #  token = RefreshToken(base64_encoded_token_string)

        token.blacklist()
        res = {'msg': 'User logged out'}
        return Response(res)


