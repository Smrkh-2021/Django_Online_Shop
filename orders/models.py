from django.db import models
from django.utils.datetime_safe import datetime
from products.models import Product, BaseDiscount
from customers.models import Customer, Address
from django.utils.translation import gettext_lazy as _
# Create your models here.
from core.models import BaseModel


class Status(BaseModel):
    """
     Status Model: This is Status of Order/Cart that contain: Paide, UnPaide, Canceled
    """
    class Meta:
        verbose_name = _("Status")
        verbose_name_plural = _("Statuses")

    title = models.CharField(verbose_name=_('Order Status'), max_length=50, unique=True)

    def __str__(self):
        return f'{self.title}'


class OffCode(BaseDiscount):
    """
     Offcode Model: This is Discount Code for Order/Cart
    """

    class Meta:
        verbose_name = _("Off Code")
        verbose_name_plural = _("Off Codes")

    code = models.CharField(verbose_name=_('off code'), max_length=50)

    def offcode_finalprice(self, price):
        if self.expire_time >= datetime.now().date():
            if self.type == 'price':
                final_price = price - self.value
                return final_price if final_price > 0 else 0
            elif self.type == 'percent':
                return price - int(price * (self.value / 100))
        return price

    def __str__(self):
        return f'Off Code: {self.value} {self.type}'


class Order(BaseModel):
    """
     Order Model: This is Order/Cart that have mane Order Items
    """

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    address = models.ForeignKey(to=Address, on_delete=models.RESTRICT, null=True, blank=True)
    offcode = models.ForeignKey(OffCode, on_delete=models.CASCADE, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    final_price = models.PositiveIntegerField(default=0, verbose_name=_('Final Price'), help_text=_("Final Price"))
    total_price = models.PositiveIntegerField(default=0, verbose_name=_('Total Price'), help_text=_("Total Price"))

    def __str__(self):
        return f'Order for Customer: {self.customer.user}'


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

    def __str__(self):
        return f"Order id: {self.order.id}, {self.product.name}, quntity:{self.count}"


    def total_price(self):
        """
        Calculate Total Price of Order Item by Mutliply Count in Product Price
        """
        return self.product.price * self.count

    def final_price(self):
        """
        Calculate Total Price of Order Item by Mutliply Count in Product Discounted Price
        """
        return self.product.discounted_price() * self.count


