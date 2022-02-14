from django.db import models
from products.models import Product
from django.utils.translation import gettext_lazy as _
# Create your models here.
from core.models import BaseModel



class Offcode(BaseModel):
    ...



class Order(BaseModel):
    ...



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




