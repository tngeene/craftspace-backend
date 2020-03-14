from rest_framework.permissions import BasePermission, SAFE_METHODS

#limit upload of products to artists only
class IsArtistOrDisallow(BasePermission):
    message = "Oops, you need to be an artist to perform this action"
    def has_permission(self, request, view):
        if request.user.membership_type != 'Artist':
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.uploaded_by == request.user
