from rest_framework.permissions import BasePermission, SAFE_METHODS

# limit editing of events to people who uploaded the event or staff

class IsOwnerorAdmin(BasePermission):
    message = 'You need to be an artist to perform this action'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return (obj.uploaded_by == request.user) or request.user.is_staff