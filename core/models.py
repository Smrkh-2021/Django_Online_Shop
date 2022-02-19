from datetime import timedelta
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from .validators import Validation
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
        # print('datetime:', datetime.now().date())
        # print('type datetime:', type(datetime.now().date()))
        # print('expire_time:', self.expire_time)
        # print('type expire_time:', type(self.expire_time))
        if self.expire_time >= datetime.now():
            if self.type == 'price':
                return min(self.value, price)
            else:  # percent
                raw_profit = int((self.value/100) * price)
                return int(min(raw_profit, int(self.max_price))) if self.max_price else raw_profit
        else:
            return 0


class MyUserManager(UserManager):
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_superuser(username, email, password, **extra_fields)



class User(AbstractUser):
    """
    User Model for Change Default User Name to Phone Number for Auth Pages
    """

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    objects = MyUserManager()
    phone = models.CharField(max_length=13, unique=True,
                             verbose_name=_("phone number"), validators=[Validation.check_phone], help_text=_("Enter your phone number"))
    USERNAME_FIELD = 'phone'