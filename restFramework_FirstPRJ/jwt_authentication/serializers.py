from dataclasses import field
from rest_framework import serializers
from .models import JWT_AuthToken

class JWT_AuthTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model=JWT_AuthToken
        fields='__all__'