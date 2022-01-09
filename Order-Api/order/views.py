from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .api.serializers import OrderSerializer

@api_view(['GET', 'POST', 'DELETE'])
def order(request):
  if request.method == 'GET':
    ordersSerializer = OrderSerializer
    orders = Order.objects.all()
    return Response({"results": ordersSerializer(orders, many=True).data })

  if request.method == 'POST':
    serializer = OrderSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
@api_view(['DELETE', 'GET'])
def orderDetails(request, id):
  try:
    order = Order.objects.get(id=id)
  except Order.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    ordersSerializer = OrderSerializer
    return Response(ordersSerializer(order).data)
  
  if request.method == 'DELETE':
    order.delete()
    return Response(status=status.HTTP_200_OK)