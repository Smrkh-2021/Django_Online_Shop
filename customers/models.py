from django.db import models
from core.models import BaseModel, User
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Customer(BaseModel):
    """
    Customer class for whoes to see products and categories and create new Orders
    """
    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.username}'


class Address(BaseModel):
    """
    Adress Class for customer's addresses
    """
    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    province = models.CharField(max_length=30, verbose_name=_('province'))
    city = models.CharField(max_length=30, verbose_name=_('city'))
    street = models.CharField(max_length=50, verbose_name=_('street'))
    alley = models.CharField(max_length=50, verbose_name=_('alley'))
    number = models.PositiveIntegerField(verbose_name=_('number'))
    description = models.TextField(help_text=_("Enter your extra description of your address"), null=True, blank=True, verbose_name=_('description'))
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('customer'))

    def __str__(self):
        return f'Address Customer: {self.customer}'


