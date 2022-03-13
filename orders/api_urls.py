from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api_views import OrderItemViewSet, OrderViewSet
from .views import *


router = DefaultRouter()
router.register('orderitem', OrderItemViewSet)
router.register('order', OrderViewSet)

urlpatterns = router.urls


# urlpatterns = [
#     path("", include(router.urls)),
#     path("", include(router.urls)),
#     # path('product_list_api/', ProductListCreateApi.as_view(), name='product_list_api'),
#     # path('order_api/<int:pk>', OrderDetailApi.as_view(), name='order_detail_api'),
# ]