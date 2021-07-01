from django.shortcuts import render, redirect
from . models import  DatosAbogado
from .forms import AbogadoForm
# Create your views here.


def home(request):
    return render(request, 'core/index.html')

def contactanos(request):
    return render(request, 'core/contactanos.html')

def abogados(request):
    abogados = DatosAbogado.objects.all()
    return render(request,'core/crud.html', {'abogados': abogados})

def form_crud(request):
    contexto = {
             'form': AbogadoForm()
        }
    if request.method == 'POST':
            formulario = AbogadoForm(request.POST)
            if formulario.is_valid():
                formulario.save()
                contexto['mensaje'] = "Abogado agregado"
    return render(request, 'core/form_crud.html', contexto)


def mod_form_crud(request, id):
    contexto = {}
    if request.method == 'POST':
        abogado = DatosAbogado.objects.get(rut = id)
        formulario = AbogadoForm(data=request.POST, instance=abogado)
        if formulario.is_valid:
            formulario.save()
            contexto['form'] = formulario
            contexto['mensaje'] = "Abogado modificado"  
    else:
       abogado = DatosAbogado.objects.get(rut = id)  
       contexto['form'] = AbogadoForm(instance=abogado) 
    return render(request, 'core/mod_form_crud.html', contexto)



def mod_eliminar_crud(request, id):
    abogado = DatosAbogado.objects.get(rut = id)
    abogado.delete()
    return redirect(to="form_crud")