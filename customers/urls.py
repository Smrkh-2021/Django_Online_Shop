from django.urls import path
from .views import CustomerLoginView, CustomerSignupView, CustomerLogoutView

# ProductListApi, ProductDetailApi,

app_name = 'customers'

urlpatterns = [
    path('login/', CustomerLoginView.as_view(), name='login_view'),
    path('logout/', CustomerLogoutView.as_view(), name='logout_view'),
    path('register/', CustomerSignupView.as_view(), name='register_view'),

]