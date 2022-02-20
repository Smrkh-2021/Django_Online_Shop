from django.urls import path
from .views import loginView
# ProductListApi, ProductDetailApi,

app_name = 'customers'

urlpatterns = [
    path('', LoginView.as_view(), name='login_view'),

]