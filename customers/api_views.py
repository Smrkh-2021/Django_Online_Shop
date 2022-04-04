from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Address, Customer
from customers.serializers import *


class AddressViewSet(viewsets.ModelViewSet):
    """
    class view for addresses in customer panel
    """
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

    def create(self, request, *args, **kwargs):
        user = self.request.user
        customer = Customer.objects.get(user=user)
        request.data._mutable = True
        request.data['customer'] = customer.id
        return super().create(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    """
    view for user profile in customer panel
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    print('areeeeeee')

    def list(self, request, *args, **kwargs):
        user = request.user
        context = {
            'user': user
        }
        template_string = render_to_string(template_name='customers/panel_profile.html', context=context)
        return JsonResponse({'user':template_string})

    def update(self, request, *args, **kwargs):
        print(self.request.data)
        if self.request.data.get('old_password'):
            old_password = self.request.data['old_password']
            print('old_password:', old_password)
            new_password = self.request.data['new_password1']
            confirm_password = self.request.data['new_password2']
            form = PasswordChangeForm(self, {'old_password': old_password, 'new_password1': new_password,
                                             'new_password2': confirm_password})
            if form.is_valid():
                form.save()
                return Response(status=200)
            else:
                return Response({'errors': form.errors.values()}, status=400)
        return super().update(request, *args, **kwargs)





