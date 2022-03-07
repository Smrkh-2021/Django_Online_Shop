from django.http import HttpResponse
from rest_framework import viewsets, generics

from .models import OrderItem, Order
from .serializers import OrderItemSerializer, OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    # def set_cookie(self, request):
    #     user = request.user
    #     if not user.is_authenticated:
    #         resp = HttpResponse()
    #         resp.set_cookie()


class Test(generics.ListCreateAPIView):
    ...