from django.contrib import admin
from .models import *
from core.admin import LogicalAdminModel
# Register your models here.


class DiscountAdmin(LogicalAdminModel):
    list_display = ['value', 'type', 'max_price', 'expire_time']
    list_display_links = ['value', 'type', 'max_price']
    list_filter = ['value', 'type', 'expire_time']
    search_fields = ['value', 'type', 'expire_time']


class CategoryAdmin(LogicalAdminModel):
    list_display = ['name', 'parent', 'discount', 'image']
    list_display_links = ['name', 'parent']
    list_filter = ['name', 'parent']
    search_fields = ['name', 'parent']

class BrandAdmin(LogicalAdminModel):
    list_display = ['name', 'country']
    list_display_links = ['name', 'country']
    list_filter = ['name', 'country']
    search_fields = ['name', 'country']

class CommentAdmin(LogicalAdminModel):
    list_display = ['title', 'content']
    list_display_links = ['title', 'content']
    list_filter = ['title', 'content']
    search_fields = ['title', 'content']


class ProductAdmin(LogicalAdminModel):
    list_display = ['name', 'price', 'discount', 'count', 'brand', 'category']
    list_display_links = ['name', 'price', 'discount']
    list_filter = ['name', 'price', 'discount']
    search_fields = ['name', 'price', 'discount']


admin.site.register(Discount, DiscountAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)