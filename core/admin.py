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

    actions = ['logical_delete']


# admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)