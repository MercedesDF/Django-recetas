from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from .models import Receta
from .forms import RecetaForm

def lista_recetas(request):
    recetas = Receta.objects.all()
    
    if request.method == "GET":
        buscar = request.GET.get('buscar', '')
        if buscar:
            recetas = recetas.filter(
                models.Q(nombre__icontains=buscar) | 
                models.Q(ingredientes__icontains=buscar) | 
                models.Q(instrucciones__icontains=buscar)
            )
    
    return render(request, 'recetas/lista_recetas.html', {'recetas': recetas})

def agregar_receta(request):
    if request.method == "POST":
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_recetas')
    else:
        form = RecetaForm()
    return render(request, 'recetas/agregar_receta.html', {'form': form})

def eliminar_receta(request, id):
    receta = get_object_or_404(Receta, id=id)
    if request.method == "POST":
        receta.delete()
        return redirect('lista_recetas')
    return render(request, 'recetas/eliminar_receta.html', {'receta': receta})
