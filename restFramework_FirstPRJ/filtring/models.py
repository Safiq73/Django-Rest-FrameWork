from django.db import models

# Create your models here.

class Filtring(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField( max_length=50)
    rollNum=models.IntegerField()
    passedby=models.CharField( max_length=50)