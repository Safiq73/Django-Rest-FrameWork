from dataclasses import field
from rest_framework import serializers
from .models import Throtttling

class ThrotttlingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Throtttling
        fields='__all__'