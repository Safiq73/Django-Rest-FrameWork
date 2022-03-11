from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=500)
    id=models.AutoField(primary_key=True)
    city=models.CharField(max_length=500)
    number=models.IntegerField(max_length=11)
    