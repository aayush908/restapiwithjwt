from rest_framework.permissions import BasePermission

class Mypermission(BasePermission):
    def has_permission(Self , request , view):
        if request.method == "POST":
            return True
        return False