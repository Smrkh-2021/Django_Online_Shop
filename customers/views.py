from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import LoginForm
from django.utils.translation import gettext_lazy as _
from .models import Customer
# Create your views here.



class CustomerLoginView(FormView):
    form_class = LoginForm
    template_name = 'customers/login.html'
    success_url = reverse_lazy('customers:login_view')
    success_message = _("Wellcome") + " %(username)s !"

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     kwargs['loginform'] = LoginForm()
    #     kwargs['signupform'] = RegistrationForm()
    #     return super().get_context_data(**kwargs)


#
# class RegistrationView(FormView):
#     model_class = RegistrationForm
#     template_name = 'customers/login.html'
#     success_url = reverse_lazy('products/home')
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
#
#     def form_invalid(self, form):
#         return super().form_invalid(form)


    # def get_context_data(self, **kwargs):
    #     kwargs['login_form'] = LoginForm()
    #     kwargs['signup_form'] = RegistrationForm()
    #     return super().get_context_data(**kwargs)





