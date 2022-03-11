from dataclasses import field
from rest_framework import serializers
from .models import ProductDetails

class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductDetails
        fields='__all__'