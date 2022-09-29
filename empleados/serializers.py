from dataclasses import fields
import imp
from rest_framework import serializers
from .models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ( 'codigo', 'nif', 'nombre', 'apellido1', 'apellido2')