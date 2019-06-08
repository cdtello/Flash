from django.db import models
from django.contrib.auth.models import User

# Create your models here.

    
class Rol(models.Model):
    idRol = models.IntegerField(primary_key = True) # Llave Primaria
    nombreRol = models.CharField(max_length = 50)
    descripcion = models.TextField()
    
class Usuario(models.Model):
    ESTADOS = (("True", "Habilitado"), ("False", "Deshabilitado"))
    identificacion = models.IntegerField(primary_key = True) # Llave Primaria
    contrasena = models.CharField(max_length = 70)
    nombre = models.CharField(max_length = 50)
    edad   = models.IntegerField()
    telefono_movil = models.CharField(max_length = 10)
    telefono_fijo = models.CharField(max_length = 10)
    direccion = models.TextField()
    email = models.EmailField()
    estado = models.CharField(max_length = 10, choices = ESTADOS)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)    # Llave Foranea
    
    def __str__(self):
        return self.nombre