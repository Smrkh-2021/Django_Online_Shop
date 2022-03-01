from django.contrib import admin
from.models import *
# Register your models here.

class AddressInLine(admin.StackedInline):
    model = Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ['province', 'city', 'street', 'alley', 'number', 'description']
    list_display_links = ['province', 'city', 'description']
    list_filter = ['province', 'city', 'street']
    search_fields = ['province', 'city']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'phone', 'email', 'user']
    list_display_links = ['phone', 'fname', 'email']
    list_filter = ['user']
    inlines = [AddressInLine, ]
    search_fields = ['fname', 'lname']



admin.site.register(Customer, CustomerAdmin)
admin.site.register(Address, AddressAdmin)