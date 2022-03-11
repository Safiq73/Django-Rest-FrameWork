from dataclasses import field
from rest_framework import serializers
from .models import Bsic_Authentication

class Bsic_AuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bsic_Authentication
        fields='__all__'