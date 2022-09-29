from pyexpat import model
from django.db import models

# Create your models here.
class Empleado(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nif = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)


