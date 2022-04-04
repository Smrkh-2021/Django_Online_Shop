import logging
# Create your views here.
from django.shortcuts import render
from django.views import View


class TestView(View):
    def get(self):
        logging.getLogger()





def handler_404(request, *args):
    # return render(request, 'pages/404.html')
    return render(request, 'pages/404.html', {}, status=404)