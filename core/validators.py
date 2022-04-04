import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def check_phone(value):
    patter1 = re.compile("^9\d{9}$")
    patter2 = re.compile("^09\d{9}$")
    patter3 = re.compile("^00989\d{9}$")
    patter4 = re.compile("^\+989\d{9}$")

    if patter1.match(value):
        return "0" + value
    if patter2.match(value):
        return value
    if patter3.match(value):
        return "0" + value[4:]
    if patter4.match(value):
        return "0" + value[3:]

    raise ValidationError(_('Phone number must be in the true IR format'))
