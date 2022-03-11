from pyexpat import model
from django.db import models

# Create your models here.

class StudentDetails(models.Model):
    name=models.CharField(max_length=500)
    id=models.IntegerField(max_length=500, primary_key=True)
    city=models.CharField(max_length=500)
    
    def __str__(self):
        return self.name