from django.urls import path , include
from apps.usuario.views import *
from django.contrib.auth import views as auth_views
from apps.usuario import views

app_name = 'usuario'

urlpatterns = [
    path('', index, name = 'index'),
    path('nuevo/', UsuarioCreate.as_view(), name ='usuario_crear'),
    path('listar/', UsuarioList.as_view(), name ='usuario_listar'),
    path('editar/<pk>', UsuarioUpdate.as_view(), name ='usuario_editar'),
    path('eliminar/<pk>', UsuarioDelete.as_view(), name ='usuario_eliminar'),
    
    path('documento/listar', RolList.as_view(), name ='rol_listar'),
    path('documento/nuevo', RolCreate.as_view(), name ='rol_crear'),
]