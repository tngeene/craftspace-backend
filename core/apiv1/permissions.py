from rest_framework.permissions import BasePermission, SAFE_METHODS

# limit upload of events by artist only

class IsArtistOrDissallow(BasePermission):
    message = 'You need to be an artist to upload or update events'

    def has_permission(self, request, view):
        if request.user.membership_type != 'Artist':
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.uploaded_by == request.user