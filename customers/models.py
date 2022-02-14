from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Customer(BaseModel):
    """
    Customer class for whoes to see products and categories and create new Orders
    """
    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)


class Address(BaseModel):
    """
    Adress Class for customer's addresses
    """
    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    province = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=50)
    alley = models.CharField(max_length=50)
    number = models.PositiveIntegerField()
    description = models.TextField(help_text=_("Enter your extra description of your address"))
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
