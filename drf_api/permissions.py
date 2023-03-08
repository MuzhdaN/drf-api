from rest_framework import permissions


"""
Adding permission to check if the user is 
the owner of the profile
"""

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
