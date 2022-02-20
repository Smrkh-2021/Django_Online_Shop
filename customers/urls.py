from django.urls import path
from .views import CustomerLoginView

# ProductListApi, ProductDetailApi,

app_name = 'customers'

urlpatterns = [
    path('', CustomerLoginView.as_view(), name='login_view'),

]