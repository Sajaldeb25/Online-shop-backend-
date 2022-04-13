from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from shop.serializers import RegisterSerializer, LoginSerializer, ProductSerializer, ProductCreateSerializer,\
    CategorySerializer
from .models import Categories, Products


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
        category = Categories.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None): # to create categories
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductView(APIView):
    def get(self, request):
        product = Products.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ProductCreateSerializer(data=request.data)

        try:
            if Categories.objects.get(id=request.data['product_category']):
                if serializer.is_valid():
                    serializer.save()
                    details_serializer = ProductSerializer(instance=serializer.instance)
                    return Response(details_serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Categories.DoesNotExist:
            res = {'msg': 'Category does not exists.'}
            return Response(res)







