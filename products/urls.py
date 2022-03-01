from django.urls import path
from .views import *
# ProductListApi, ProductDetailApi,

app_name = 'products'

urlpatterns = [
    path('', ProductView.as_view(), name='product_list_view'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_Detail_view'),
    path('productlist/', ProductListView.as_view(), name='product_list'),
]

