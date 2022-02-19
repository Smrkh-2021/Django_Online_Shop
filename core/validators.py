import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Validation():

    def check_phone(self, value):
        patter1 = re.compile("^9\d{9}$")
        patter2 = re.compile("^09\d{9}$")
        patter3 = re.compile("^00989\d{9}$")
        patter4 = re.compile("^\+989\d{9}$")

        if bool(patter1.match(value)):
            return "0" + value
        if bool(patter2.match(value)):
            return value
        if bool(patter3.match(value)):
            return "0" + value[4:]
        if bool(patter4.match(value)):
            return "0" + value[3:]

        raise ValidationError(_('Phone number must be in the true IR format'))

