# cart/urls.py

from django.urls import path
from .views import CartView, CartItemView 

urlpatterns = [
  
    path('cart/', CartView.as_view(), name='cart-view'),

  
    path('cart/items/<int:item_id>/', CartItemView.as_view(), name='cart-item-view'),
]