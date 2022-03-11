from django.db import models
from django.forms import EmailField

# Create your models here.

class Pgination(models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField( max_length=50)
    last_name=models.CharField( max_length=50)
    email=EmailField(max_length=254)
    gender=models.CharField( max_length=50)