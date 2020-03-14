from rest_framework.permissions import BasePermission, SAFE_METHODS

#limit making of orders to collectors only
class IsCollectorOrIsAdmin(BasePermission):
    message = "Oops, you need to be a collector to perform this action"

    def has_permission(self, request, view):
    # allow all post requests for collectors
        if request.user.membership_type != 'Collector':
            if request.method == 'POST':
                return True
            #  otherwise only authenticated requests
            return request.user and request.user.is_staff
        return False

