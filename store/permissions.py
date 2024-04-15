from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        # Allow GET, HEAD or OPTIONS requests (read-only permissions)
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        
        # Only authenticated users can modify objects
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow read-only permissions for non-authenticated users
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        
        # Only the owner of the object can modify it
        return obj.seller == request.user
