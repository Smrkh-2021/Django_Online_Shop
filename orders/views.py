from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem
# Create your views here.


# class CartListView(ListView):
#     """
#     class view for display order items
#     """
#     model = OrderItem
#     template = 'cart.html'



# class OrderItemDetailApi(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = OrderItemSerializer
#     queryset = Order.objects.all()
#     # template_name = 'profile_list.html'
#
#
# class OrderDetailApi(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = OrderSerializer
#     queryset = Order.objects.all()
#     renderer_classes = [TemplateHTMLRenderer]
#
#     def put(self, request, *args, **kwargs):
#         return super().put(request, *args, **kwargs)
#
#
#
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return Response({'user': self.object}, template_name='orders/cart.html')