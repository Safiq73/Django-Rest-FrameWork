
from rest_framework import serializers
from .models import Crud_ModelViewSet

class Crud_ModelViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Crud_ModelViewSet
        fields='__all__'