from re import M
from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre = models.CharField(max_length=35)
    edad = models.PositiveBigIntegerField()
    nacimiento = models.DateTimeField()