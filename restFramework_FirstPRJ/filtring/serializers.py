from dataclasses import field
from rest_framework import serializers
from .models import Filtring

class FiltringSerializer(serializers.ModelSerializer):
    class Meta:
        model=Filtring
        fields='__all__'