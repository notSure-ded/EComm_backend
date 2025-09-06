

from rest_framework import serializers
from .models import Cart, CartItem
from products.models import Product

class CartProductSerializer(serializers.ModelSerializer):
    """
    A minimal serializer for the Product model to be nested in CartItemSerializer.
    """
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image_url']


class CartItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the CartItem model.
    """
  
    product = CartProductSerializer(read_only=True)
 
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']

    def get_total_price(self, obj):
     
        return obj.product.price * obj.quantity


class CartSerializer(serializers.ModelSerializer):
    """
    Serializer for the Cart model.
    """
   
    items = CartItemSerializer(many=True, read_only=True)
   
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'grand_total']

    def get_grand_total(self, obj):
        
        total = 0
        for item in obj.items.all():
            total += item.product.price * item.quantity
        return total