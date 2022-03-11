
from dataclasses import field
from rest_framework import serializers
from .models import Student


# class StudentSerializers(serializers.Serializer):
#     name=serializers.CharField(max_length=50)   #these are same as model fields instead of models.CharField(max_length=50)
#     rollNum=serializers.CharField(max_length=50)
#     city=serializers.CharField(max_length=50)

class StudentSerializers(serializers.ModelSerializer ):
    def starts_with_a(value):
        if value[0]!='a':
            raise serializers.ValidationError('Name should start with A')
    name=serializers.CharField(max_length=500, validators=[starts_with_a]) 
    class Meta:
        model = Student
        fields=['rollNum', 'city']
        
        
        
        
