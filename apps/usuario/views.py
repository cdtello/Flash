from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.usuario.forms import UsuarioForm, RolForm
from apps.usuario.models import Usuario, Rol
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'usuario/index.html')

def usuario_delete(request, id_empleado):
    empleado = Usuario.objects.get(identificacion = id_empleado)
    if request.method == 'POST':
        empleado.delete()
        return redirect('usuario_listar')
    return render(request, 'usuario/usuario_delete.html',{'usuario':empleado})
    

class UsuarioList(ListView):
    model = Usuario
    template_name='usuario/usuario_list.html'

class UsuarioCreate(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/usuario_form.html'
    success_url = reverse_lazy('usuario:usuario_listar')

class UsuarioUpdate(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/usuario_form.html'
    success_url = reverse_lazy('usuario:usuario_listar')
    
class  UsuarioDelete(DeleteView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/usuario_delete.html'
    success_url = reverse_lazy('usuario:usuario_listar')
    
    
    
    
class RolList(ListView):
    model = Rol
    template_name = 'rol/rol_list.html'
    
class RolCreate(CreateView):
    model = Rol
    template_name = 'rol/rol_form.html'
    form_class = RolForm
    second_form_class = UsuarioForm
    success_url = reverse_lazy('usuario:rol_listar')
    
class RolUpdate(UpdateView):
    model = Rol
    form_class = RolForm
    template_name = 'rol/rol_form.html'
    success_url = reverse_lazy('usuario:rol_listar')
    
class  RolDelete(DeleteView):
    model = Rol
    form_class = RolForm
    template_name = 'rol/rol_delete.html'
    success_url = reverse_lazy('usuario:rol_listar')