from django.db import models
from core.models import BaseModel, User
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Customer(BaseModel):
    """
    Customer model for somebody to see products and categories and create new Orders
    """
    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f'{self.phone}'


class Address(BaseModel):
    """
    Adress Class for customer's addresses
    """
    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    province = models.CharField(max_length=30, verbose_name=_('province'), null=True, blank=True)
    city = models.CharField(max_length=30, verbose_name=_('city'), null=True, blank=True)
    street = models.CharField(max_length=50, verbose_name=_('street'), null=True, blank=True)
    alley = models.CharField(max_length=50, verbose_name=_('alley'), null=True, blank=True)
    number = models.PositiveIntegerField(verbose_name=_('number'), null=True, blank=True)
    description = models.TextField(help_text=_("Enter your extra description of your address"), null=True, blank=True, verbose_name=_('description'))
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('customer'))

    def __str__(self):
        return f'Address Customer: {self.customer} is: {self.province}'


