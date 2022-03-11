from rest_framework import serializers
from .models import Employee

class EmployeeSerialization(serializers.Serializer):
    name=serializers.CharField(max_length=500)
    id=serializers.IntegerField()
    city=serializers.CharField(max_length=500)

    def create(self, validate_data):
        return Employee.objects.create(**validate_data )
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name', instance.name)
        instance.city=validated_data.get('city', instance.city)
        instance.number=validated_data.get('number', instance.number)
        instance.save()
        return instance 