from django.urls import path , include
from apps.usuario.views import *
from django.contrib.auth import views as auth_views
from apps.usuario import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
app_name = 'usuario'

urlpatterns = [
    path('index/', index, name = 'index'),
    
    path('salir', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='usuario/login.html'),name='login'),
    
    path('listar/', login_required(UsuarioList.as_view()), name ='usuario_listar'),
    path('editar/<pk>', login_required(UsuarioUpdate.as_view()), name ='usuario_editar'),
    path('eliminar/<pk>', login_required(UsuarioDelete.as_view()), name ='usuario_eliminar'),
    
    path('rol/nuevo', login_required(RolCreate.as_view()), name ='rol_crear'),
    path('rol/listar', login_required(RolList.as_view()), name ='rol_listar'),
    path('rol/editar/<pk>', login_required(RolUpdate.as_view()), name ='rol_editar'),
    path('rol/eliminar/<pk>', login_required(RolDelete.as_view()), name ='rol_eliminar'),
    
    path('registrar/', login_required(RegistroUsuario.as_view()), name ='usuario_registrar'),
    
    
]