from django.db import models
from products.models import Product
from customers.models import Customer
from django.utils.translation import gettext_lazy as _
# Create your models here.
from core.models import BaseModel, BaseDiscount


class Status(BaseModel):
    """
     Status Model: This is Status of Order/Cart that contain: Paide, UnPaide, Canceled
    """
    class Meta:
        verbose_name = _("Off code")
        verbose_name_plural = _("Off codes")

    title = models.CharField(verbose_name=_('Order Status'), max_length=50, unique=True)


class OffCode(BaseDiscount):
    """
     Offcode Model: This is Discount Code for Order/Cart
    """

    class Meta:
        verbose_name = _("Offcode")
        verbose_name_plural = _("Offcodes")

    code = models.PositiveIntegerField(verbose_name=_('off code'), help_text=_("Off Code"), null=True, blank=True)


class Order(BaseModel):
    """
     Order Model: This is Order/Cart that have mane Order Items
    """

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    offcode = models.ForeignKey(OffCode, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    final_price = models.PositiveIntegerField(default=0, verbose_name=_('Final Price'), help_text=_("Final Price"))
    total_price = models.PositiveIntegerField(default=0, verbose_name=_('Total Price'), help_text=_("Total Price"))


class OrderItem(BaseModel):
    """
     OrderItem Model: for Items in Cart or Order
    """

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")

    count = models.PositiveIntegerField(default=0, verbose_name=_('Count'), help_text=_("OrderItem Count"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
