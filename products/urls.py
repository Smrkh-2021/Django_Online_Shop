from django.urls import path
from .views import ProductListApi, ProductDetailApi, ProductView


app_name = 'products'

urlpatterns = [
    path('', ProductView.as_view(), name='product_list_view'),
    path('product_list_api/', ProductListApi.as_view(), name='product_list_api'),
    path('product_api/<int:pk>', ProductDetailApi.as_view(), name='product_detail_api'),
]

