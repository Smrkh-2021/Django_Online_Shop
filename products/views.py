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
    """
    class view for display detail of a product
    """
    model = Product
    template_name = 'products/product_detail.html'


class ProductListView(ListView):
    """
    class view for display products of one category
    """
    model = Product
    template_name = 'products/product_list.html'

    def get_queryset(self):
        print('dict', dict(self.request.GET))
        filters = dict(self.request.GET)
        try:
            for key, value in filters.items():
                filters[key] = ''.join(value)
                # print('filters', filters)
            # print('filtersss', filters)
            # print('return', Product.objects.filter(category__name='Engine', price__lte=5800, price__gte=4800))
            return Product.objects.filter(**filters)
        except Exception as e:
            print(e)
            return super().get_queryset()

# def get_context_data(self, *, object_list=None, **kwargs):
#     # print('llll',self.request.GET.get(object_list))
#     kwargs['category_products'] = Product.objects.filter(category_id=category_id)
#     return super().get_context_data(object_list=object_list, **kwargs)

##################################### API View ######################################


class ProductListApi(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        cat_id = self.kwargs['pk']
        return Product.objects.filter(category_id=cat_id)


class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


# class ProductListCreateApi(generics.ListCreateAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()
#
#     def get_queryset(self):
#         filters = dict(self.request.GET)
#         try:
#             for key, value in filters.items():
#                 filters[key] = ''.join(value)
#             return Product.objects.filter(**filters)
#         except Exception:
#             return super().get_queryset()
