from django.contrib import admin
from.models import *
from core.admin import LogicalAdminModel
# Register your models here.

class AddressInLine(admin.StackedInline):
    model = Address


class AddressAdmin(LogicalAdminModel):
    list_display = ['province', 'city', 'street', 'alley', 'number', 'description', 'customer']
    list_display_links = ['province', 'city', 'description']
    list_filter = ['province', 'city', 'street']
    search_fields = ['province', 'city']


class CustomerAdmin(LogicalAdminModel):
    list_display = ['phone', 'user']
    list_display_links = ['phone']
    list_filter = ['user']
    inlines = [AddressInLine, ]
    search_fields = ['phone', 'user']



admin.site.register(Customer, CustomerAdmin)
admin.site.register(Address, AddressAdmin)