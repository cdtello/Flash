from django import forms
from apps.usuario.models import Usuario,Rol

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
             
        ]
        
        labels = {
            'username'      :   'Nombre de Usuario',
            'first_name'    :   'Nombre',
            'last_name'     :   'Apellidos',
            'email'         :   'Correo',  
        }

class UsuarioForm(forms.ModelForm):
     
    class Meta:
        model = Usuario
         
        fields = [
            'identificacion', 
            'telefono', 
            'rol',
        ]
        labels = {
            'identificacion'            : 'Identificación', 
            'telefono'                  : 'Telefono Movil', 
            'rol'                       : 'Rol',
        }
        widgets = {
            'identificacion'            : forms.TextInput(attrs={'class':'form-control'}), 
            'telefono'                  : forms.TextInput(attrs={'class':'form-control'}), 
        }

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = [
            'idRol',
            'nombreRol',
            'descripcion',
        ]
        labels = {
            'idRol'                 :   'Id Rol',
            'nombreRol'             :   'Nombre Rol',
            'descripcion'           :   'Descripcion',
        }
        widgets = {
            'idRol'                 :   forms.TextInput(attrs={'class':'form-control'}), 
            'nombreRol'             :   forms.TextInput(attrs={'class':'form-control'}), 
            'descripcion'           :   forms.TextInput(attrs={'class':'form-control'}), 
        }
        

