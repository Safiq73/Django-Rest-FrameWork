
from .models import CRUD_Auth_Token
from rest_framework import viewsets
from .serializers import CRUD_Auth_TokenSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .customauthentication import CustomAuthentication
# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=CRUD_Auth_Token.objects.all()
    serializer_class=CRUD_Auth_TokenSerializer
    authentication_classes=[CustomAuthentication]
    permission_classes=[IsAuthenticated]