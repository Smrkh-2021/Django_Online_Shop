from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import ListView
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem
# Create your views here.



class OrderItemDeleteView(generics.DestroyAPIView):
    """
    class view for delete order item in cart
    """
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()





class OrderItemListView(ListView):
    """
    class view for display order items in cart
    """
    model = OrderItem
    template_name = 'orders/cart.html'
    context_object_name = 'items'

    def get_queryset(self):
        return OrderItem.objects.filter(order__customer__user=self.request.user)



class OrderListView(ListView):
    model = Order

    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(customer__user=self.request.user)
        context = {
            'orders': orders
        }
        template_string = render_to_string(template_name='customers/panel_order.html')
        return JsonResponse({'order':template_string})

