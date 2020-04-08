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
    
    #custom permission to allow only owner to edit the resource
class IsOwnerOrReadOnly(BasePermission):
    message = 'Oops, You need to be the owner to update the profile'

    def has_object_permission(self, request, view, obj):
        #Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
         return True
        return obj.user == request.user