from rest_framework import serializers
from .models import Pgination

class PginationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pgination
        fields='__all__'