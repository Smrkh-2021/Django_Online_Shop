from django.http import JsonResponse
from django.template.loader import render_to_string
from rest_framework import viewsets
from .models import Address, Customer
from customers.serializers import *


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    def list(self, request, *args, **kwargs):
        address = Address.objects.filter(customer__user=self.request.user)
        print(address)
        context = {
            'addresses': address
        }
        template_string = render_to_string(template_name='customers/panel_address.html', context=context)
        return JsonResponse({'address':template_string})

    def destroy(self, request, *args, **kwargs):
        print("delete")
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        print('update')
        return super().update(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        user = request.user
        context = {
            'user': user
        }
        template_string = render_to_string(template_name='customers/panel_profile.html', context=context)
        return JsonResponse({'user':template_string})



