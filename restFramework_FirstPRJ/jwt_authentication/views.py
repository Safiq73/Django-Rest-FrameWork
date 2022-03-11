
from .models import JWT_AuthToken
from rest_framework import viewsets
from .serializers import JWT_AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=JWT_AuthToken.objects.all()
    serializer_class=JWT_AuthTokenSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]