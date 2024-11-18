from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


class IsAdminOrModerator(BasePermission):
    """
    Is Admin User permission to only allow admin users to write.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == 1
        )
