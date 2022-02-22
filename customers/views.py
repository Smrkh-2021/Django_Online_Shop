from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from .forms import LoginForm, RegistrationForm
from django.utils.translation import gettext_lazy as _
from .models import Customer
# Create your views here.



class CustomerLoginView(FormView):
    form_class = LoginForm
    template_name = 'customers/login.html'
    success_url = reverse_lazy('products:product_list_view')
    success_message = _("Wellcome")

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        login(self.request, form.get_user())
        user = self.request.user
        Customer.objects.get_or_create(user=user)
        return super().form_valid(form)



#
class CustomerSignupView(FormView):
    form_class = RegistrationForm
    template_name = 'customers/register.html'
    success_url = reverse_lazy('products:product_list_view')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)



class CustomerLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('products:product_list_view'))


