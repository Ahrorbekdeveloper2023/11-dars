from rest_framework.permissions import BasePermission, SAFE_METHODS


class DailyCostPermissions(BasePermission):
    
    def has_permission(self, request, view):
        if request.method == SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            return True


    def has_object_permission(self, request, view, obj):
        if request.method == SAFE_METHODS:
            return True

        if request.user == obj.user_id:
            return True

