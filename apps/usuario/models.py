from django.db import models
from django.contrib.auth.models import User

# Create your models here.

    
class Rol(models.Model):
    idRol = models.IntegerField(primary_key = True) # Llave Primaria
    nombreRol = models.CharField(max_length = 50)
    descripcion = models.TextField()
    
class Usuario(models.Model):
    user =  models.OneToOneField(User,on_delete=models.CASCADE, primary_key = True) # Llave Primaria
    identificacion = models.IntegerField(default = 0)
    telefono = models.CharField(max_length = 10)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)    # Llave Foranea
    
    def __str__(self):
        return self.nombre