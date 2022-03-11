from django.db import models

# Create your models here.

class Users(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=500)
    city=models.CharField(max_length=500)
    number=models.IntegerField(max_length=11)