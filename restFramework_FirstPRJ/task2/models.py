from django.db import models

# Create your models here.

class Manager(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.EmailField(max_length=254, unique=True)
    password=models.CharField(max_length=254)
    name=models.CharField( max_length=50)
    salary=models.IntegerField()
    department=models.CharField( max_length=50)