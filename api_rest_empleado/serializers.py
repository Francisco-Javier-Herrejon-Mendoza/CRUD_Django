from rest_framework import serializers
from crud.models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['idEmpleado', 'nombre', 'apellido', 'correo', 'telefono']