from django.shortcuts import render
from django.views.generic import FormView
from .models import Customer
# Create your views here.



class LoginView(FormView):
    model = Customer