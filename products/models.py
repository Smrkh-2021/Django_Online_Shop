from django.db import models
from django.utils.datetime_safe import datetime
from datetime import timedelta
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _

# Create your models here.

def get_default_my_date():
    return datetime.now() + timedelta(days=10)

class BaseDiscount(BaseModel):
    expire_time = models.DateField(null=True, default=get_default_my_date)
    max_price = models.PositiveIntegerField(null=True, blank=True)
    value = models.PositiveIntegerField(null=False, default=0)
    type = models.CharField(max_length=10, choices=[('price', 'Price'), ('percent', 'Percent')], null=False)
    def profit_value(self, price: int):
        """
        Calculate and Return the profit of the discount
        :param price: int (item value)
        :return: profit
        """
        if self.expire_time >= datetime.now():
            if self.type == 'price':
                return min(self.value, price)
            else:  # percent
                raw_profit = int((self.value/100) * price)
                return int(min(raw_profit, int(self.max_price))) if self.max_price else raw_profit
        else:
            return 0

    class Meta:
        abstract = True


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
    image = models.FileField(upload_to='category', verbose_name=_('category image'))

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


    name = models.CharField(max_length=50, verbose_name=_('product name'))
    price = models.IntegerField(verbose_name=_('price'))
    image_main = models.FileField(upload_to='products', verbose_name=_('product main image'), help_text='main image')
    image_accessories = models.FileField(upload_to='products', verbose_name=_('product accessory image'), help_text='accessory image')
    stock = models.PositiveIntegerField(default=1, help_text=_("Number of Products item in Repository"), verbose_name=_('product count in stock'))
    color = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name=_('product color'))
    dimension = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name=_('product dimenssion'))
    weight = models.CharField(max_length=20, null=True, blank=True, default=None, verbose_name=_('product weight'))
    properties = models.TextField(help_text=_("Enter Details of your products"), null=True, blank=True, default=None, verbose_name=_('product properties'))
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True, default=None)


    def discounted_price(self):
        if self.discount.expire_time >= datetime.now().date():
            if self.discount.type == 'price':
                res = self.price - self.discount.value
                return res if res > 0 else 0
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



