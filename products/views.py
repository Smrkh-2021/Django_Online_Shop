from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins, generics
from .serializers import ProductSerializer
from .models import Product
# Create your views here.

from django.views.generic import ListView
from products.models import Product

class ProductView(ListView):
    model = Product
    template_name = 'products/home.html'


class ProductListApi(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()