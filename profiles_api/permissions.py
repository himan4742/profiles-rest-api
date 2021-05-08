from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Returns True or False whether to allow permission or not"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
