from django.urls import path
from .views import *
from .api_views import OrderItemViewSet


app_name = 'orders'

urlpatterns = [
    path('', OrderItemListView.as_view(), name='orderitem_list'),
    path('delitem/<int:pk>', OrderItemDeleteView.as_view(), name='orderitem_delete'),
    path('panelorders/', OrderListView.as_view(), name='panel_orders_list')
]

