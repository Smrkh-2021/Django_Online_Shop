from rest_framework.routers import DefaultRouter
from django.urls import path, include
from customers.api_views import *





router = DefaultRouter()

router.register('address', AddressViewSet)
router.register('user', UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]