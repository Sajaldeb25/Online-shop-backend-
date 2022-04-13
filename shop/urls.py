from django.urls import path
from shop.views import RegisterView, LoginView, CategoryView, ProductView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('category/', CategoryView.as_view(), name='category'),
    path('product/', ProductView.as_view(), name='product')
]
