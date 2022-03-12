from django.urls import path
from .views import *
from .api_views import OrderItemViewSet


app_name = 'orders'

urlpatterns = [
    path('', OrderItemListView.as_view(), name='orderitem_list')
]

