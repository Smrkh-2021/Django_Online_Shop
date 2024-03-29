import re

from django.core.exceptions import ValidationError


def phone_validator(value):
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

    raise ValidationError(f'{value} is not a valid phone')