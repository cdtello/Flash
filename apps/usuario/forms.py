from django import forms
from apps.usuario.models import Usuario,Rol


class UsuarioForm(forms.ModelForm):
     
    class Meta:
        model = Usuario
         
        fields = [
            'identificacion', 
            'contrasena',
            'nombre',
            'edad',
            'telefono_movil', 
            'telefono_fijo',
            'direccion', 
            'email', 
            'estado',
        ]
        labels = {
            'identificacion'            : 'Identificación', 
            'contrasena'                : 'Contraseña',
            'nombre'                    : 'Nombre',
            'edad'                      : 'Edad',
            'telefono_movil'            : 'Telefono Movil', 
            'telefono_fijo'             : 'Telefono Fijo',
            'direccion'                 : 'Dirección', 
            'email'                     : 'Email', 
            'estado'                    : 'Estado',
        }
        widgets = {
            'identificacion'            : forms.TextInput(attrs={'class':'form-control'}), 
            'contrasena'                : forms.TextInput(attrs={'class':'form-control'}),
            'nombre'                    : forms.TextInput(attrs={'class':'form-control'}),
            'edad'                      : forms.TextInput(attrs={'class':'form-control'}),
            'telefono_movil'            : forms.TextInput(attrs={'class':'form-control'}), 
            'telefono_fijo'             : forms.TextInput(attrs={'class':'form-control'}),
            'direccion'                 : forms.TextInput(attrs={'class':'form-control'}), 
            'email'                     : forms.TextInput(attrs={'class':'form-control'}), 
            'estado'                    : forms.TextInput(attrs={'class':'form-control'}),  
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
