from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from .validators import check_phone
# Create your models here.
from django.utils.datetime_safe import datetime


class MyBaseManager(models.Manager):
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

    objects = MyBaseManager()
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
        self.save()


class MyUserManager(UserManager):
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_superuser(username, email, password, **extra_fields)

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_user(username, email, password, **extra_fields)

class User(AbstractUser):

    """
    Custome User Model for Change Default User Name to Phone Number
    """
    USERNAME_FIELD = 'phone'
    phone = models.CharField(max_length=13, unique=True,validators=[check_phone] , verbose_name=_("phone number"), help_text=_("Enter your phone number"))
    # birthdate = models.DateField(default=None, null=True, blank=True, verbose_name=_("Birth Date"))
    gender = models.CharField(max_length=7, default=None, null=True, blank=True,
                              choices=[('male', 'MALE'), ('female', 'FEMALE')], verbose_name=_("Gender"))
    objects = MyUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def save(self, *args, **kwargs):
        self.username = self.phone
        # if User.objects.filter(id=self.id):
        #     self.set_password(self.password)
        super().save(*args, **kwargs)










