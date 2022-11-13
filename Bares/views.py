from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bares, Restaurantes, Heladerias, Avatar
from .forms import Bar_formulario, Restaurante_formulario, Heladeria_formulario, Buscar_formulario, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    avatar = Avatar.objects.get(user=request.user)
    return render(request, 'inicio.html', {'url': avatar.imagen.url})

# CREACIÓN DE LISTAS

class BaresList(ListView):
    model = Bares
    template_name = 'bares.html'
    context_object_name = "listabares"

class RestaurantesList(ListView):
    model = Restaurantes
    template_name = 'restaurantes.html'
    context_object_name = "listarestaurantes"

class HeladeriasList(ListView):
    model = Heladerias
    template_name = 'heladerias.html'
    context_object_name = "listaheladerias"

# VISTAS DE DETALLE

class BaresDetail(DetailView):
    model = Bares
    template_name = 'bares_detalle.html'

# CREACIÓN DE ELEMENTOS

class BaresCreate(CreateView):
    model = Bares
    template_name = 'bares_create.html'
    fields = ["nombre", "email", "telefono"]
    success_url = "/app-bares/bares/"

class RestaurantesCreate(CreateView):
    model = Restaurantes
    template_name = 'restaurantes_create.html'
    fields = ("__all__")
    success_url = "/app-bares/restaurantes/"

class HeladeriasCreate(CreateView):
    model = Heladerias
    template_name = 'heladerias_create.html'
    fields = ("__all__")
    success_url = "/app-bares/heladerias/"

# ACTUALIZAR OBJETOS

class BaresUpdate(UpdateView):
    model = Bares
    template_name = 'bares_update.html'
    fields = ("__all__")
    success_url = "/app-bares/bares/"
    context_object_name = "bares"

class RestaurantesUpdate(UpdateView):
    model = Restaurantes
    template_name = 'restaurantes_update.html'
    fields = ("__all__")
    success_url = "/app-bares/restaurantes/"
    context_object_name = "restaurantes"

class HeladeriasUpdate(UpdateView):
    model = Heladerias
    template_name = 'heladerias_update.html'
    fields = ("__all__")
    success_url = "/app-bares/heladerias/"
    context_object_name = "heladerias"

# ELIMINAR OBJETOS

class BaresDelete(LoginRequiredMixin, DeleteView):
    model = Bares
    template_name = 'bares_delete.html'
    success_url = "/app-bares/bares/"

class HeladeriasDelete(LoginRequiredMixin, DeleteView):
    model = Heladerias
    template_name = 'heladerias_delete.html'
    success_url = "/app-bares/heladerias/"

class RestaurantesDelete(LoginRequiredMixin, DeleteView):
    model = Restaurantes
    template_name = 'restaurantes_delete.html'
    success_url = "/app-bares/restaurantes/"

# BUSCAR REGISTROS
@login_required
def buscar_restaurante (request):
    resto_busqueda= request.GET['restaurante']
    restoran= Restaurantes.objects.filter(nombre=resto_busqueda)
    return render(request, 'resultado_restaurante.html', {'restaurante': restoran, 'query': resto_busqueda})

def buscar_bar (request):
    bar_busqueda= request.GET['bar']
    mi_bar= Bares.objects.filter(nombre=bar_busqueda)
    return render(request, 'resultado_bar.html', {'bar': mi_bar, 'query': bar_busqueda})

def buscar_heladeria (request):
    heladeria_busqueda= request.GET['heladeria']
    mi_heladeria= Heladerias.objects.filter(nombre=heladeria_busqueda)
    return render(request, 'resultado_heladeria.html', {'heladeria': mi_heladeria, 'query': heladeria_busqueda})

# USUARIOS
def login_view(request):
    if request.method == 'POST':
        miFormulario = AuthenticationForm(request, data=request.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]
            user = authenticate(username=usuario, password=psw)
            if user:
                login(request, user)
                return render(request, 'inicio.html', {"mensaje": f"Bienvendido {usuario}"})
            else:
                return render(request, 'inicio.html', {"mensaje": f"Error, datos incorrectos"})
        return render(request, 'inicio.html', {"mensaje": f"Error, formulario invalido"})   
        
    else:
        miFormulario = AuthenticationForm()
        return render(request, 'login.html', {'miFormulario': miFormulario})

def register(request):
    if request.method == 'POST':
        miFormulario = UserCreationForm(request.POST)

        if miFormulario.is_valid():
            username = miFormulario.cleaned_data["username"]
            miFormulario.save()
            return render(request, 'inicio.html', {"mensaje": f"Usuario {username} creado con éxito."})
        else:
            return render(request, 'inicio.html', {"mensaje": "Error al crear el usuario."})
    else:
        miFormulario = UserCreationForm()
        return render(request, 'registro.html', {'miFormulario': miFormulario})

def editar_perfil(request):
    usuario = request.user

    if request.method =='POST':
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data['password1'])
            
            usuario.save()

            return render(request, 'inicio.html', {"mensaje": "Datos actualizados"})

        return render(request, 'editar_perfil.html', {"mensaje": "Las constraseñas no coinciden"})
        
    else:
        miFormulario = UserEditForm(instance=request.user)
        return render(request, 'editar_perfil.html', {"miFormulario": miFormulario})
