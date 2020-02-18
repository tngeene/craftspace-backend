from rest_framework.permissions import BasePermission,SAFE_METHODS

# limit creation of artist profile to artist only

class IsArtistOrDissallow(BasePermission):
    message = 'Oops,you need to be an artist to update artist profile'

    def has_permission(self, request, view):
        if request.user.membership_type != 'Artist':
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user

#limit creation of collector profile to collector only

class IsCollectorOrDissallow(BasePermission):
    message = 'Oops, You need to be a collector to perform this action'
    def has_permission(self, request, view):
        if request.user.membership_type != 'Collector':
            return False
        return True
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user