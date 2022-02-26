from django.urls import path
from .views import *

# ProductListApi, ProductDetailApi,

app_name = 'customers'

urlpatterns = [
    path('login/', CustomerLoginView.as_view(), name='login_view'),
    path('logout/', CustomerLogoutView.as_view(), name='logout_view'),
    path('register/', CustomerSignupView.as_view(), name='register_view'),
    path('user_list/', UserListApi.as_view(), name='user_listview'),
    path('user_detail/<int:pk>', UserDetailApi.as_view(), name='user_detailview'),
    path('address_list/', AddressListApi.as_view(), name='address_listview'),
]
