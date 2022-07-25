from django.db import models

# Create your models here.

class Empleado(models.Model):
    idEmpleado = models.AutoField(primary_key=True, verbose_name="ID Empleado")
    nombre = models.CharField(max_length=150, blank=True, null=True)
    apellido = models.CharField(max_length=150, blank=True, null=True)
    correo = models.CharField(max_length=150, blank=True, null=True)
    telefono = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'empleado'