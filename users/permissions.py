from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """Проверяет является ли пользователь модератором."""
    message = 'Adding customers not allowed.'

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderators').exists()


class IsOwner(permissions.BasePermission):
    """Проверяет, является ли пользователь модератором."""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
