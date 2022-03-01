import logging

from django.shortcuts import render

# Create your views here.
from django.views import View


class TestView(View):
    def get(self):
        logging.getLogger()