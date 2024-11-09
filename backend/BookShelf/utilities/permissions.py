from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


class IsAdminUser(BasePermission):
    """
    Is Admin User permission to only allow admin users to write.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to admin users.
        # return request.user and request.user.is_staff
        return request.user and request.user.is_authenticated and request.user.role == 1
