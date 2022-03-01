from django.contrib import admin
from .models import *
# Register your models here.



class StatusAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']


class OffCodeAdmin(admin.ModelAdmin):
    list_display = ['code']
    list_filter = ['code']
    search_fields = ['code']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['address', 'offcode', 'status', 'customer', 'final_price', 'total_price']
    list_display_links = ['address', 'offcode', 'customer']
    list_filter = ['customer', 'address']
    search_fields = ['address', 'customer']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['count', 'product', 'order']
    list_display_links = ['count', 'product', 'order']
    list_filter = ['product', 'order']
    search_fields = ['product', 'order']



admin.site.register(Status, StatusAdmin)
admin.site.register(OffCode, OffCodeAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
