import generics as generics
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins, generics
from .serializers import ProductSerializer

# Create your views here.
from django.views.generic import ListView, DetailView
from products.models import Product, Category


class ProductView(ListView):
    model = Product
    template_name = 'products/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['root_categories'] = Category.objects.filter(parent=None)
        return super().get_context_data(object_list=object_list, **kwargs)



class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'





class ProductListApi(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


