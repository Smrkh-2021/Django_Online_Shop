from django.contrib import admin
from .models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'discount', 'count', 'brand', 'category']
    # list_display_links = ['phone', 'fname']
    # list_filter = ['phone']
    # inlines = [AddressInLine, ]
    # search_fields = ['fname', 'lname']







admin.site.register(Discount)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)