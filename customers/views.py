from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, ListView
from requests import Response
from rest_framework import generics, authentication
from .forms import LoginForm, RegistrationForm
from django.utils.translation import gettext_lazy as _
from .models import Customer
# Create your views here.
from .permissions import IsOwner, IsSuperUser
from .serializers import *
from .utils import save_orderitems_from_cookie_to_db

class CustomerSignupView(FormView):
    """
    class view for signup anonymous user
    """

    form_class = RegistrationForm
    template_name = 'customers/register.html'
    success_url = reverse_lazy('products:product_list_view')

    def form_valid(self, form):
        form.clean_phone()
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)




class CustomerLoginView(FormView):
    """
    class view for login user after signup
    """
    form_class = LoginForm
    template_name = 'customers/login.html'
    success_url = reverse_lazy('products:product_list_view')
    success_message = _("Wellcome")

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        url = self.request.GET.get('next', None)
        if url:
            self.success_url = url
        login(self.request, form.get_user())
        user = self.request.user
        Customer.objects.get_or_create(user=user)
        response = super().form_valid(form)
        if self.request.COOKIES.get('cookie_product'):
            save_orderitems_from_cookie_to_db(self.request)
            response.delete_cookie('cookie_product')
        return response



class CustomerLogoutView(View):
    def get(self, request):
        logout(request)
        response = HttpResponseRedirect(reverse_lazy('products:product_list_view'))
        # if self.request.COOKIES.get('cookie_product'):
        #     response.delete_cookie('cookie_product')
        return response





# class UserListApi(generics.ListCreateAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     permission_classes = [IsSuperUser]
#     authentication_classes = [authentication.BasicAuthentication]
#
#
#
# class UserDetailApi(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     permission_classes = [IsOwner]
#     authentication_classes = [authentication.BasicAuthentication]
#
#
#
# class AddressListApi(generics.ListCreateAPIView):
#     serializer_class = AddressSerializer
#     queryset = Address.objects.all()
#     permission_classes = [IsSuperUser]
#     authentication_classes = [authentication.BasicAuthentication]
#
#     def get_queryset(self):
#         customer = Customer.objects.get(user=self.request.user)
#         return Address.objects.filter(customer=customer)
#
#
#
#
# class AddressDetailApi(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = AddressSerializer
#     queryset = Address.objects.all()
#
#     authentication_classes = [authentication.BasicAuthentication]


class CustomerPanelView(LoginRequiredMixin, ListView):
    template_name = 'customers/panel.html'
    queryset = Customer.objects.all()
    login_url = '/customers/login'
