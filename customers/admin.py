from django.contrib import admin
from.models import *
# Register your models here.

class AddressInLine(admin.StackedInline):
    model = Address


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'phone', 'email', 'user']
    list_display_links = ['phone', 'fname']
    list_filter = ['phone']
    inlines = [AddressInLine, ]
    search_fields = ['fname', 'lname']



admin.site.register(Customer, CustomerAdmin)
admin.site.register(Address)