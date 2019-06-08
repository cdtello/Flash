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
    success_url = reverse_lazy('usuario_listar')

class UsuarioUpdate(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/usuario_form.html'
    success_url = reverse_lazy('usuario_listar')
    
class  UsuarioDelete(DeleteView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/usuario_delete.html'
    success_url = reverse_lazy('usuario_listar')
    
class RolList(ListView):
    model = Rol
    template_name = 'usuario/rol_list.htm'
    
class RolCreate(CreateView):
    model = Rol
    template_name = 'usuario/rol_form.htm'
    form_class = RolForm
    second_form_class = UsuarioForm
    success_url = reverse_lazy('rol_listar')
    
    def get_context_data(self, **kwargs):
        context = super(RolCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            documento = form.save(commit=False)
            documento.empleado = form2.save()
            documento.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))