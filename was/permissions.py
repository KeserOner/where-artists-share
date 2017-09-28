from rest_framework.permissions import BasePermission, SAFE_METHODS

from artists.models import Artists


class IsAuthenticatedAndIsOwner(BasePermission):

    message = 'current user not matching user trying to update user'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated():
            if hasattr(obj, 'user'):
                return request.user == obj.user
            else:
                artist = Artists.objects.get(user=request.user)
                return artist == obj.artist
