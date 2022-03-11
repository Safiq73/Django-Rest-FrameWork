
from django.db import models


# Create your models here.

class Bsic_Authentication(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField( max_length=50)
    price=models.IntegerField()
    category=models.CharField( max_length=50)