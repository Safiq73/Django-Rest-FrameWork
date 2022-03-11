
from .models import Bsic_Authentication
from rest_framework import viewsets
from .serializers import Bsic_AuthenticationSerializer
from rest_framework.authentication import BasicAuthentication , SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly , DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from .custompermssion import MyPermission

# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Bsic_Authentication.objects.all()
    serializer_class=Bsic_AuthenticationSerializer
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAdminUser]
    # authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticatedOrReadOnly]
    
    # authentication_classes=[SessionAuthentication]
    # permission_classes=[DjangoModelPermissions]
    
    
    # authentication_classes=[SessionAuthentication]
    # permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    
    authentication_classes=[SessionAuthentication]
    permission_classes=[MyPermission]
    