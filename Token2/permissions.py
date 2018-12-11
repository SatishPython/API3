from rest_framework.permissions import BasePermission,SAFE_METHODS
class IsAdminOrReadOnly(BasePermission):
    def Premission1(self,request,view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.User.is_staff