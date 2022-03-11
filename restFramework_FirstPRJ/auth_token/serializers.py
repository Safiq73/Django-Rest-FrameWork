from dataclasses import field
from rest_framework import serializers
from .models import CRUD_Auth_Token

class CRUD_Auth_TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model=CRUD_Auth_Token
        fields='__all__'