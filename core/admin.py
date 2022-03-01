from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group

from .models import User
# Register your models here.

class LogicalAdminModel(admin.ModelAdmin):
    """
    custom admin model for logical options
    """
    def logical_delete(self, request, queryset):
        queryset.update(is_delete=True)


    def deactivate(self, request, queryset):
        queryset.update(is_active=False)


    def activate(self, request, queryset):
        queryset.update(is_delete=False, is_active=True)


    actions = ['logical_delete', 'activate', 'deactivate']


# admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)