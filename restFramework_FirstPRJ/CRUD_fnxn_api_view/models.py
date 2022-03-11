
from django.db import models
from django.forms import CharField


# Create your models here.

class Teacher(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField( max_length=50)
    rollNum=models.IntegerField()
    city=models.CharField( max_length=50)