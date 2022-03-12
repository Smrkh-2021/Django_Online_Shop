from django.http import HttpResponse
from rest_framework import viewsets, generics

from customers.models import Customer
from .models import OrderItem, Order
from .serializers import OrderItemSerializer, OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def update(self, request, *args, **kwargs):
        coupon = request.data['coupon']
        print(coupon)
        return super().update(request, *args, **kwargs)


class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()

    def create(self, request, *args, **kwargs):
        print('1')
        if self.request.user.is_authenticated:
            print('2')
            user = request.user
            customer = Customer.objects.get_or_create(user=user)[0]
            order = Order.objects.get_or_create(customer=customer, status_id=4)[0]
            request.data._mutable = True
            request.data['order'] = order.id
            return super().create(request, *args, **kwargs)

    # def set_cookie(self, request):
    #     user = request.user
    #     if not user.is_authenticated:
    #         resp = HttpResponse()
    #         resp.set_cookie()


class Test(generics.ListCreateAPIView):
    ...