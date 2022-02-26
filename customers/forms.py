from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .validators import phone_validator
from django.utils.translation import gettext_lazy as _
from core.models import User


class LoginForm(AuthenticationForm):

    help_texts = {
        'username': _("Phone"),
        'password': _("Password"),
    }

    def clean_username(self):
        phone = self.cleaned_data['username']
        valid_phone = phone_validator(phone)
        return valid_phone


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['phone', 'password1', 'password2']

        help_texts = {
            'phone': _("Phone"),
            'password1': _("Password"),
            'password2': _("Confirm Password"),
        }

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        valid_phone = phone_validator(phone)
        return valid_phone

