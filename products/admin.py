from django.contrib import admin
from .models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'discount', 'count', 'brand', 'category']
    list_display_links = ['name', 'price', 'discount']
    list_filter = ['name', 'price', 'discount']
    # inlines = [AddressInLine, ]
    search_fields = ['name', 'price', 'discount']


class DiscountAdmin(admin.ModelAdmin):
    list_display = ['value', 'type', 'max_price', 'count', 'expire_time']
    list_display_links = ['value', 'type', 'max_price']
    list_filter = ['value', 'type', 'expire_time']
    # inlines = [AddressInLine, ]
    search_fields = ['value', 'type', 'expire_time']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'discount', 'image']
    list_display_links = ['name', 'parent']
    list_filter = ['name', 'parent']
    # inlines = [AddressInLine, ]
    search_fields = ['name', 'parent']

class BrandAdmin(admin.ModelAdmin):
    ...

class CommentAdmin(admin.ModelAdmin):
    ...

admin.site.register(Discount, DiscountAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)