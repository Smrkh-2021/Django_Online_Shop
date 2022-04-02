from django.http import HttpResponse
import json
from rest_framework import viewsets, generics
from django.template.loader import render_to_string
from rest_framework.response import Response

from customers.models import Customer
from products.models import Product
from .models import OrderItem, Order, Status, OffCode
from .serializers import OrderItemSerializer, OrderSerializer
from .utils import set_cart_cookie, list_of_orderitems_from_cookie, number_of_orderitems_in_cookie


class OrderViewSet(viewsets.ModelViewSet):
    """
    class for calculate coupon discount in cart and return final price
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def update(self, request, *args, **kwargs):
        coupon = request.data['coupon']
        sub_total_str = request.data['sub_total'][:-1]
        sub_total = int(sub_total_str)
        print('coupon is:', coupon)
        print('sub_total is:', sub_total)
        try:
            offcode = OffCode.objects.get(code=coupon)
            offcode_id = offcode.id
            request.data._mutable = True
            request.data['offcode'] = offcode_id
            final_price = offcode.offcode_finalprice(sub_total)
            final_price = str(final_price) + '$'
            print('final_price:', final_price)
            value = str(offcode.value)
            type = offcode.type
            if type=='price':
                discount_coupon = value + '$'
            else:
                discount_coupon = value + '%'
            super().update(request, *args, **kwargs)
            print('discount_coupon:', discount_coupon)
            resp = Response({'final_price': final_price, 'discount_coupon': discount_coupon}, status=200)
            return resp
        except:
            return Response(status=400)


class OrderItemViewSet(viewsets.ModelViewSet):
    """
    class for create orderitems and order in cart
    """
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()

    def create(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            user = request.user
            customer = Customer.objects.get_or_create(user=user)[0]
            order = Order.objects.get_or_create(customer=customer, status_id=3)[0]
            same_orderitems = OrderItem.objects.filter(order=order, product_id=request.data['product'])
            if same_orderitems:
                orderitem = same_orderitems[0]
                orderitem.count += 1
                orderitem.save()
                return Response(status=201)
            request.data._mutable = True
            request.data['order'] = order.id
            return super().create(request, *args, **kwargs)
        else:
            cookie = set_cart_cookie(request)
            response = Response(status=201)
            response.set_cookie('cookie_product', cookie)
            return response

    # def get_queryset(self):
    #     # cookie = self.request.COOKIES.get('cookie_product')
    #     if self.request.user.is_authenticated():
    #         user = self.request.user
    #         customer = Customer.objects.get_or_create(user=user)[0]
    #         order = Order.objects.get(customer=customer, status_id=3)
    #         return order.orderitem_set.all()
    #     else:
    #         orderitem_list = list_of_cookie_to_orderitem(self.request)
    #         return orderitem_list

    # def set_cookie(self, request):
    #     user = request.user
    #     if not user.is_authenticated:
    #         resp = HttpResponse()
    #         resp.set_cookie()


class OrderListView(generics.ListAPIView):
    """
    class base view for show orders in customer panel
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


    def get_queryset(self):
        queryset = Order.objects.filter(customer__user=self.request.user)
        return queryset


class OrderUpdateView(generics.UpdateAPIView):
    """
    class for update status of order after checkout
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def perform_update(self, serializer):
        user = self.request.user
        customer = Customer.objects.get(user=user)
        order = Order.objects.get(customer=customer, status_id=3)
        serializer.validated_data['status'] = Status.objects.get(id=2)
        print(serializer.validated_data['status'])
        super().perform_update(serializer)




