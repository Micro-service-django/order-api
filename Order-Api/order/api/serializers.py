from django.db.models import fields
from rest_framework import serializers
from ..models import Order, Product

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = (
      'id', 
      'name', 
      'weight', 
      'price'
    )

class OrderSerializer(serializers.ModelSerializer):
  product = ProductSerializer(read_only=True)
  
  class Meta:
    model = Order
    fields = (
      'id', 
      'value_order', 
      'email', 
      'name', 
      'product', 
      'created_at', 
      'updated_at'
    )