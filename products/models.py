from django.db import models
from django.utils.datetime_safe import datetime

from core.models import BaseModel, BaseDiscount
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Discount(BaseDiscount):
    """
     Discount Model: for Apply discount on Product Price
    """
    class Meta:
        verbose_name = _("Discount")
        verbose_name_plural = _("Discounts")

    title = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}: {self.value} {self.type}'


class Category(BaseModel):
    """
     Category Model: for Apply discount on Product Price
    """
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, default=None)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.name}'


class Brand(BaseModel):
    """
     Brand Model: for brand producer of all Products
    """
    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")


    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Product(BaseModel):
    """
     Product Model: for all Products to show in home page
    """
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


    name = models.CharField(max_length=50, verbose_name=_('prodect name'))
    price = models.PositiveIntegerField(verbose_name=_('price'))
    image = models.FileField(upload_to='products', verbose_name=_('product image'))
    count = models.PositiveIntegerField(help_text=_("Number of Products item in Repository"), verbose_name=_('product count'))
    color = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name=_('product color'))
    dimension = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name=_('product dimenssion'))
    weight = models.CharField(max_length=20, null=True, blank=True, default=None, verbose_name=_('product weight'))
    properties = models.TextField(help_text=_("Enter Details of your products"), null=True, blank=True, default=None, verbose_name=_('product properties'))
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True, default=None)


    def discounted_price(self):
        if self.discount.expire_time >= datetime.now().date():
            if self.discount.type == 'price':
                res = self.price - self.discount.value
                return res
            elif self.discount.type == 'percent':
                res = self.price - int(self.price * (self.discount.value / 100))
                return res
        return self.price


    def __str__(self):
        return f'{self.name}'


class Comment(BaseModel):
    """
     Comment Model: for all Products comments that shows in detail view
    """

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")


    title = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField(help_text=_("Enter Text Demand"))
