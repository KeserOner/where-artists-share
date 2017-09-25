from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthenticatedAndIsOwner(BasePermission):

    message = 'current user not matching user trying to update user'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated():
            if request.user == obj.user:
                return True
        return False
