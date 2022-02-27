from django.urls import path
from .views import *
# ProductListApi, ProductDetailApi,

app_name = 'products'

urlpatterns = [
    path('', ProductView.as_view(), name='product_list_view'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_Detail_view'),
    path('productlist/', ProductListView.as_view(), name='product_list'),
    # path('product_list_api/', ProductListApi.as_view(), name='product_list_api'),
    # path('product_api/<int:pk>', ProductDetailApi.as_view(), name='product_detail_api'),
]

