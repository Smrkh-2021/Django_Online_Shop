from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import ListView
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .utils import list_of_orderitems_from_cookie
from customers.models import Customer
from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem
# Create your views here.



class OrderItemListView(ListView):
    """
    class view for display order items in cart in two mode: authenticated(from database) or anonymous(from coookie)
    """
    model = OrderItem
    template_name = 'orders/cart.html'
    context_object_name = 'items'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            print('user', user)
            customer = Customer.objects.get(user=user)
            print('customer', customer)
            order = Order.objects.get_or_create(customer=customer, status_id=3)[0]
            return order.orderitem_set.all()
        else:
            try:
                list_orderitem = list_of_orderitems_from_cookie(self.request)
                return list_orderitem
                # return OrderItem.objects.filter(order__customer__user=self.request.user)
            except:
                return []




class OrderListView(ListView):
    """
    class for show orders list in customer panel
    """
    model = Order

    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(customer__user=self.request.user)
        context = {
            'orders': orders
        }
        template_string = render_to_string(template_name='customers/panel_order.html', context=context)
        return JsonResponse({'order':template_string})

