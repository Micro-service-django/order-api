from django.urls import path

from .views import order, orderDetails

urlpatterns = [
  path('order/', order),
  path('order/<str:id>', orderDetails),
]