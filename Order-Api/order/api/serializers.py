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
  product = ProductSerializer(many=False)
  
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
  
  def create(self, validated_data):
    product = validated_data.pop('product')
    product = Product.objects.create(**product)
    return Order.objects.create(product_id=product.id, **validated_data)