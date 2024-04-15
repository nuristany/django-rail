from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the item.
        if obj.seller == request.user:
            return True
        else:
            # If the requesting user is not the owner, return a custom response
            return Response("You do not have permission to perform this action.", status=status.HTTP_403_FORBIDDEN)
