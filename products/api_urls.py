from django.urls import path
from .views import *
# ProductListApi, ProductDetailApi,

# app_name = 'products'

urlpatterns = [
    # path('product_list_api/', ProductListCreateApi.as_view(), name='product_list_api'),
    path('product_api/<int:pk>', ProductDetailApi.as_view(), name='product_detail_api'),
]