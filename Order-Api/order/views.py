from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order, Product
from .api.serializers import OrderSerializer, ProductSerializer

@api_view(['GET', 'POST'])
def order(request):
  ordersSerializer = OrderSerializer
  if request.method == 'GET':
    orders = Order.objects.all()
    return Response({"results": ordersSerializer(orders, many=True).data }, status=201)

  if request.method == 'POST':
    serializer = OrderSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    product_serializer = ProductSerializer(data=request.data['product'])
    product_serializer.is_valid(raise_exception=True)
    product_serializer.save()
    print(product_serializer)
    serializer.product = product_serializer
    serializer.save()

    return Response(OrderSerializer(order).data, status=201)