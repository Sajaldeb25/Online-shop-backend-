from django.urls import path
from shop.views import RegisterView, LoginView, CategoryView, ProductView, CartItemView, BlacklistRefreshView, UserOrderedItemView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('category/', CategoryView.as_view(), name='category'),
    path('product/', ProductView.as_view(), name='product'),
    path('cartitem/', CartItemView.as_view(), name='cart item'),
    path('logout/', BlacklistRefreshView.as_view(), name="logout"),
    path('userorder/', UserOrderedItemView.as_view(), name="user ordered item")
]
