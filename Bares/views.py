from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bares, Restaurantes, Heladerias
from .forms import Bar_formulario, Restaurante_formulario, Heladeria_formulario, Buscar_formulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

def inicio(request):
    return render(request, 'inicio.html')

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

class BaresDelete(DeleteView):
    model = Bares
    template_name = 'bares_delete.html'
    success_url = "/app-bares/bares/"

class HeladeriasDelete(DeleteView):
    model = Heladerias
    template_name = 'heladerias_delete.html'
    success_url = "/app-bares/heladerias/"

class RestaurantesDelete(DeleteView):
    model = Restaurantes
    template_name = 'restaurantes_delete.html'
    success_url = "/app-bares/restaurantes/"

# BUSCAR REGISTROS

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