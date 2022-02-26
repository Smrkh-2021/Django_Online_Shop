from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # return request.user == obj
        return request.user.is_superuser




class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser
