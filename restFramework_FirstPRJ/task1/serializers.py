import imp
from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=500)
    city=serializers.CharField(max_length=500)
    number=serializers.IntegerField()
    
    def create(self, validate_data):
        return Users.objects.create(**validate_data )