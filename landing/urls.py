from django.urls import path
from .views import *
# ProductListApi, ProductDetailApi,

app_name = 'landing'

urlpatterns = [
    path('contactus/', ContactUsView.as_view(), name='contactus'),
    path('aboutus/', AboutView.as_view(), name='aboutus'),
]