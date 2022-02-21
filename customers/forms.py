from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from core.models import User


class LoginForm(AuthenticationForm):

    help_texts = {
        'username': _("Phone"),
        'password': _("Password"),
    }


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['phone', 'password1', 'password2']

        help_texts = {
            'phone': _("Phone"),
            'password1': _("Password"),
            'password2': _("Confirm Password"),
        }

        def clean_phone(self):
            ...