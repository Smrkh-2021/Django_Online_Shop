from django.urls import path
from .views import CustomerLoginView, CustomerSignupView

# ProductListApi, ProductDetailApi,

app_name = 'customers'

urlpatterns = [
    path('login/', CustomerLoginView.as_view(), name='login_view'),
    path('register/', CustomerSignupView.as_view(), name='register_view'),

]