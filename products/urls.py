from django.urls import path
from .views import ProductView, ProductDetailView
# ProductListApi, ProductDetailApi,

app_name = 'products'

urlpatterns = [
    path('', ProductView.as_view(), name='product_list_view'),
    path('product/<slug:name>', ProductDetailView.as_view(), name='product_Detail_view'),
    # path('product_list_api/', ProductListApi.as_view(), name='product_list_api'),
    # path('product_api/<int:pk>', ProductDetailApi.as_view(), name='product_detail_api'),
]

