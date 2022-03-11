from dataclasses import field
from rest_framework import serializers
from .models import Crud_ViewSet

class Crud_ViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Crud_ViewSet
        fields='__all__'