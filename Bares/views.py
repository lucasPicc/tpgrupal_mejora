from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bares, Restaurantes, Heladerias
from .forms import Bar_formulario, Restaurante_formulario, Heladeria_formulario, Buscar_formulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

def inicio(request):
    return render(request, 'inicio.html')

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

def bar_formulario(request):
    if request.method == 'POST':
        mi_formulario = Bar_formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            bar = Bares(nombre=data['nombre'], email=data['email'], telefono=data['telefono'])
            bar.save()
            
            return redirect('Bares')
    else:
        mi_formulario = Bar_formulario()

    return render(request, 'bar_formulario.html', {'mi_formulario':mi_formulario})

def restaurante_formulario(request):
    if request.method == 'POST':
        mi_formulario = Restaurante_formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            restaurante = Restaurantes(nombre=data['nombre'], email=data['email'], telefono=data['telefono'])
            restaurante.save()
            
            return redirect('Restaurantes')
    else:
        mi_formulario = Restaurante_formulario()

    return render(request, 'restaurante_formulario.html', {'mi_formulario':mi_formulario})

def heladeria_formulario(request):
    if request.method == 'POST':
        mi_formulario = Heladeria_formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            heladeria = Heladerias(nombre=data['nombre'], email=data['email'], telefono=data['telefono'])
            heladeria.save()
            
            return redirect('Heladerias')
    else:
        mi_formulario = Heladeria_formulario()

    return render(request, 'heladeria_formulario.html', {'mi_formulario':mi_formulario})

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

def eliminar_bar(request, id):
    bar = Bares.objects.get(id=id)
    bar.delete()
    bares = Bares.objects.all()
    return render(request, "Bares.html", {"listabares": bares})  

def editar_bar(request, id):
    bar = Bares.objects.get(id=id)
    if request.method == 'POST':
        miFormulario = Bar_formulario(request.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            bar.nombre = data["nombre"]
            bar.email = data["email"]
            bar.telefono = data["telefono"]
            bar.save()
            return redirect('Bares')
    
    else:
        miFormulario = Bar_formulario(initial={
            "nombre": bar.nombre,
            "email": bar.email,
            "telefono": bar.telefono,
        })
        return render(request, "editar_bar.html", {"miFormulario": miFormulario, "id": bar.id})