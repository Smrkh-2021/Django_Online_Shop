from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.views.generic import FormView
from django.views.generic import TemplateView
from landing.forms import ContactUsForm
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.shortcuts import render





# Create your views here.



class ContactUsView(SuccessMessageMixin, FormView):
    form_class = ContactUsForm
    success_url = reverse_lazy('landing:contactus')
    template_name = 'landing/contact.html'
    success_message = _('okkkk')


    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        send_mail(subject, message, email, ['m64.django@gmail.com', email])
        print('done')
        messages.success(self.request, _('your message sended'))
        return super().form_valid(form)



    def form_invalid(self, form):
        print('form invalid')
        print(form.errors)
        return super().form_invalid(form)


class AboutView(TemplateView):
    template_name = "landing/about.html"
