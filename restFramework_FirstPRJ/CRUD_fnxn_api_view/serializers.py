from dataclasses import field
from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=['name', 'city', 'rollNum']