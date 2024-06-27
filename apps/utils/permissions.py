# permissions.py
from rest_framework import permissions


class IsSuperuser(permissions.BasePermission):
    """
    Custom permission to allow only superusers to POST, PATCH or DELETE.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
