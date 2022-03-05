from django.urls import path
from .views import *




urlpatterns = [
    # path('product_list_api/', ProductListCreateApi.as_view(), name='product_list_api'),
    path('order_api/<int:pk>', OrderDetailApi.as_view(), name='order_detail_api'),
]