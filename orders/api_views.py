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
        try:
            sub_total = int(sub_total_str)
            offcode = OffCode.objects.get(code=coupon)
            offcode_id = offcode.id
            request.data._mutable = True
            request.data['offcode'] = offcode_id
            final_price = offcode.offcode_finalprice(sub_total)
            final_price = str(final_price) + '$'
            value = str(offcode.value)
            type = offcode.type
            if type=='price':
                discount_coupon = value + '$'
            else:
                discount_coupon = value + '%'
            super().update(request, *args, **kwargs)
            resp = Response({'final_price': final_price, 'discount_coupon': discount_coupon}, status=200)
            return resp
        except:
            return Response(status=404)


class OrderItemViewSet(viewsets.ModelViewSet):
    """
    class for create orderitems and order in cart
    """
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()

    def destroy(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            user = request.user
            customer = Customer.objects.get(user=user)
            order = Order.objects.get(customer=customer, status_id=3)
            super().destroy(request, *args, **kwargs)
            orderitem_count = OrderItem.objects.filter(order=order).count()
            resp = Response({'orderitem_count': orderitem_count}, status=200)
            return resp
        cookie_str = request.COOKIES.get('cookie_product')
        cookie_dict = json.loads(cookie_str)
        product_id = request.data['product_id']
        if cookie_dict.get(product_id):
            del cookie_dict[product_id]
        orderitem_count = len(cookie_dict)
        cookie_json = json.dumps(cookie_dict)
        response = Response({'orderitem_count': orderitem_count}, status=200)
        response.set_cookie('cookie_product', cookie_json)
        return response


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
            # resp.data['test'] = 2
            resp = super().create(request, *args, **kwargs)
            orderitem_count = OrderItem.objects.filter(order=order).count()
            resp.data['orderitem_count'] = orderitem_count
            return resp
        cookie = set_cart_cookie(request)
        orderitems_count = number_of_orderitems_in_cookie(request)
        response = Response({'orderitem_count':orderitems_count},status=201)
        response.set_cookie('cookie_product', cookie)
        return response

    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super().partial_update(request, *args, **kwargs)
        count = request.data['count']
        product_id = request.data['product']
        cookie_str = request.COOKIES.get('cookie_product')
        cookie_dict = json.loads(cookie_str)
        if cookie_dict.get(product_id):
            cookie_dict[product_id] = count
        response = Response(status=200)
        cookie_json = json.dumps(cookie_dict)
        response.set_cookie('cookie_product', cookie_json)
        return response




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
        try:
            final_price_front = int(self.request.data['final_price'])
            print('final_price_front', final_price_front)
            user = self.request.user
            customer = Customer.objects.get(user=user)
            order = Order.objects.get(customer=customer, status_id=3)
            orderitems = OrderItem.objects.filter(order=order)
            print('orderitems:', orderitems)
            final_price_bk = 0
            for orderitem in orderitems:
                final_price_bk += orderitem.product.discounted_price() * orderitem.count
                print('final_price_bk', final_price_bk)
            if order.offcode:
                final_price_bk = order.offcode.offcode_finalprice(final_price_bk)
                print('final_price_bk_offcode', final_price_bk)
            if final_price_bk == final_price_front:
                serializer.validated_data['status'] = Status.objects.get(id=2)
                print(serializer.validated_data['status'])
                super().perform_update(serializer)
        except:
            return Response(status=404)


class OrderCancelView(generics.UpdateAPIView):
    """
    class for update status of order after Canceled
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def update(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super().update(request, *args, **kwargs)
        try:
            response = Response(status=200)
            response.set_cookie('cookie_product', '')
            return response
        except:
            return Response(status=404)





