from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group

from .models import User
# Register your models here.




# admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)