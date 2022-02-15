from datetime import timedelta

from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime


class BaseManager(models.Manager):
    """
    Base Class Manager for Customize the Query Set and Filter by Deleted
    """
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False)

    def get_all(self):
        return super().get_queryset()


class BaseModel(models.Model):
    """
    Basic Class Model for Inheritance All Other Class Model from it
    """

    objects = BaseManager()
    create_datetime = models.DateTimeField(auto_now_add=True, editable=False)
    modify_datetime = models.DateTimeField(auto_now=True, editable=False)
    delete_datetime = models.DateTimeField(default=None, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False, editable=False, db_index=True)

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_delete = True
        self.save()

    def undelete(self):
        self.is_delete = False
        self.save()

    def activate(self):
        self.is_active = True
        self.save()

    def deactivate(self):
        self.is_active = False




class BaseDiscount(BaseModel):
    expire_time = models.DateField(null=True, default=lambda: datetime.now().date()+timedelta(days=2))
    max_price = models.PositiveIntegerField(null=True, blank=True)
    value = models.PositiveIntegerField(null=False)
    type = models.CharField(max_length=10, choices=[('price', 'Price'), ('percent', 'Percent')], null=False)
    def profit_value(self, price: int):
        """
        Calculate and Return the profit of the discount
        :param price: int (item value)
        :return: profit
        """
        print('datetime:', datetime.now().date())
        print('type datetime:', type(datetime.now().date()))
        print('expire_time:', self.expire_time)
        print('type expire_time:', type(self.expire_time))
        if self.expire_time >= datetime.now():
            if self.type == 'price':
                return min(self.value, price)
            else:  # percent
                raw_profit = int((self.value/100) * price)
                return int(min(raw_profit, int(self.max_price))) if self.max_price else raw_profit
        else:
            return '0'