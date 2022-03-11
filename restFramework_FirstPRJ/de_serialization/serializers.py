from wsgiref.validate import validator
from rest_framework import serializers
from .models import StudentDetails

    
def starts_with_a(value):
    # Here we can have any function name, and it is written outsid the class
    if value[0]!='a':
        raise serializers.ValidationError('Name should start with A')
    
class StudentDetailSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=500, validators=[starts_with_a]) # we have to mention validators=[starts_with_a] to call the function
    id=serializers.IntegerField()
    city=serializers.CharField(max_length=500)
    
    def create(self, validate_data):
        return StudentDetails.objects.create(**validate_data )
    
    # def validate_city(self, value):
    #     # function name should always start with validate_ followed by field name
    #     if len(value)<5:
    #         raise serializers.ValidationError('Check the value you have entered')
    #     return value    
    
    # def validate(self, data): #Here function name always validate
    #     # we will get all the fields in this type of the validation
    #     nm=data.get('name')
    #     ct=data.get('city')
    #     if len(nm)<3 or len(ct)<3:
    #         raise serializers.ValidationError('Please check the name and the city you have entered')
    #     return data