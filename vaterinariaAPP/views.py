from django.shortcuts import render,redirect
from veterinariaAPP.models import Veterinaria, Dueno, Mascota, Estetica, Vacunas, Cirugias
from django.db.models import Avg, Max, Min, Sum 
from veterinariaAPP.forms import *



# Create your views here.
def index(request):
    return render (request, 'index.html',)



def VeterinariaDataView(request):
    
    # VeterinariaDataView = VeterinariaDataView.objects.all().order_by('valor')
    # suma = VeterinariaDataView.objects.all().aggregate(Sum('valor'))
    # maximo = VeterinariaDataView.objects.all().aggregate(Max('valor'))
    # minimo = VeterinariaDataView.objects.all().aggregate(Min('valor'))

    listapacientes = Veterinaria.objects.all()
    data = {'veterina': listapacientes}
    return render(request, 'veterinaria.html', data)

def crearPaciente(request):
    form = VeterinariaForm()
    if (request.method =='POST'):
        form = VeterinariaForm(request.POST)
        if (form.is_valid()):
            
            """Rescatar los datos del formulario"""
            pacien = form.cleaned_data
            """crear el objeto paciente"""
            paciente = Veterinaria(
                nombrePaciente=pacien['nombrePaciente'],
                FechaAtencion = pacien['FechaAtencion'],
                motivo=pacien['motivo'],
                diagnostico=pacien['diagnostico'],
                tratamiento=pacien['tratamiento'], 
                observacion=pacien['observacion'],
                valor= pacien['valor']
            )
            print("datos validos")
            paciente.save()
            """Limpiar el formulario"""
            form = ''
            return redirect('/veterinaria')

    data={'form': form, 'titulo': 'Crear paciente'}
    return render(request,'crearPaciente.html', data)

def eliminarPaciente(request, id):
    paciente = Veterinaria.objects.get(id=id)
    paciente.delete()
    return redirect('/veterinaria')

def editarPaciente(request, id):
    paciente = Veterinaria.objects.get(id=id)
    form = VeterinariaForm(instance=paciente)
    if (request.method =='POST'):
        form = VeterinariaForm(request.POST, instance=paciente)
        if (form.is_valid()):
            form.save()
            return redirect('/veterinaria')
    data={'form': form, 'titulo': 'Editar paciente'}
    return render(request,'crearPaciente.html', data)


def DuenoDataView(request):
    listadueño = Dueno.objects.all()
    data = {'due': listadueño}
    return render(request, 'dueño.html', data)

def crearDueno(request):
    form = Dueno()
    if (request.method =='POST'):
        form = Dueno(request.POST)
        if (form.is_valid()):
            
            """Rescatar los datos del formulario"""
            due = form.cleaned_data
            """crear el objeto paciente"""
            dueño = Dueno(
                nombreDueño=due['nombre'],
                edad= due['edad']
            )
            print("datos validos")
            dueño.save()
            """Limpiar el formulario"""
            form = ''
            return redirect('/dueño')

    data={'form': form, 'titulo': 'Crear dueño'}
    return render(request,'creardueño.html', data)

def eliminarDueno(request, id):
    dueño = Dueno.objects.get(id=id)
    dueño.delete()
    return redirect('/dueño')

def editarDueno(request, id):
    dueño = Dueno.objects.get(id=id)
    form = Dueno(instance=dueño)
    if (request.method =='POST'):
        form = Dueno(request.POST, instance=dueño)
        if (form.is_valid()):
            form.save()
            return redirect('/dueño')
    data={'form': form, 'titulo': 'Editar dueño'}
    return render(request,'creardueño.html', data)


def MascotaDataView (request):
    listamascota = Mascota.objects.all()
    data = {'mas': listamascota}
    return render(request, 'mascota.html', data)

def crearMascota(request):
    form = Mascota()
    if (request.method =='POST'):
        form = Mascota(request.POST)
        if (form.is_valid()):
            
            """Rescatar los datos del formulario"""
            mas = form.cleaned_data
            """crear el objeto paciente"""
            mascota = Mascota(
                nombre=mas['nombre'],
                dueño= mas['dueño'],
                edad= mas['edad'],
                descripcion=mas['descripcion']
            )
            print("datos validos")
            mascota.save()
            """Limpiar el formulario"""
            form = ''
            return redirect('/mascota')

    data={'form': form, 'titulo': 'Crear dueño'}
    return render(request,'crearmascota.html', data)

def eliminarMascota(request, id):
    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    return redirect('/mascota') 

def editarMascota(request, id):
    mascota = Mascota.objects.get(id=id)
    form = Mascota(instance=mascota)
    if (request.method =='POST'):
        form = Mascota(request.POST, instance=mascota)
        if (form.is_valid()):
            form.save()
            return redirect('/mascota')
    data={'form': form, 'titulo': 'Editar mascota'}
    return render(request,'crearmascota.html', data)


def EsteticaDataView(request):
    listaestetica = Estetica.objects.all()
    data = {'est': listaestetica}
    return render(request, 'estetica.html', data)
  
def crearEstetica(request):
    form = Estetica()
    if (request.method =='POST'):
        form = Estetica(request.POST)
        if (form.is_valid()):
            
            """Rescatar los datos del formulario"""
            est = form.cleaned_data
            mascota = Estetica(
                nombrePaciente=est['nombrePaciente'],
                dueño= est['dueño'],
                edad= est['edad'],
                descripcion=est['descripcion']
            )
            print("datos validos")
            mascota.save()
            """Limpiar el formulario"""
            form = ''
            return redirect('/estetica')

    data={'form': form, 'titulo': 'Crear estetica'}
    return render(request,'crearestetica.html', data)

def eliminarestetica(request, id):
    estetica = Estetica.objects.get(id=id)
    estetica.delete()
    return redirect('/estetica') 

def editarestetica(request, id):
    estetica = Estetica.objects.get(id=id)
    form = Estetica(instance=estetica)
    if (request.method =='POST'):
        form = Estetica(request.POST, instance=estetica)
        if (form.is_valid()):
            form.save()
            return redirect('/estetica')
    data={'form': form, 'titulo': 'Editar estetica'}
    return render(request,'crearestetica.html', data)


def VacunaDataView(request):
    listaVacunas = Vacunas.objects.all()
    data = {'vac': listaVacunas}
    return render(request, 'vacuna.html', data)

def crearvacuna(request):
    form = VacunaForm()
    if (request.method =='POST'):
        form = VacunaForm(request.POST)
        if (form.is_valid()):
            
            """Rescatar los datos del formulario"""
            vac = form.cleaned_data
            """crear el objeto paciente"""
            vacuna = Vacunas(
                nombrePaciente=vac['nombrePaciente'],
                FechaAtencion = vac['FechaAtencion'],
                motivo=vac['motivo'],
                diagnostico=vac['diagnostico'],
                tratamiento=vac['tratamiento'], 
                observacion=vac['observacion'],
                valor= vac['valor']
            )
            print("datos validos")
            vacuna.save()
            """Limpiar el formulario"""
            form = ''
            return redirect('/vacuna')

    data={'form': form, 'titulo': 'Crear vacuna'}
    return render(request,'crearvacuna.html', data)

def eliminarvacuna(request, id):
    vacuna = Vacunas.objects.get(id=id)
    vacuna.delete()
    return redirect('/vacuna')

def editarvacuna(request, id):

    vacuna = Vacunas.objects.get(id=id)
    form = Vacunas(instance=vacuna)
    if (request.method =='POST'):
        form = Vacunas(request.POST, instance=vacuna)
        if (form.is_valid()):
            form.save()
            return redirect('/vacuna')
    data={'form': form, 'titulo': 'Editar vacuna'}
    return render(request,'crearvacuna.html', data)


def CirugiaDataView(request):
    listaCirugias = Cirugias.objects.all()
    data = {'cir': listaCirugias}
    return render(request, 'cirugia.html', data)

def crearcirugia(request):

    form = CirugiaForm()
    if (request.method =='POST'):
        form = CirugiaForm(request.POST)
        if (form.is_valid()):
            
            """Rescatar los datos del formulario"""
            cir = form.cleaned_data
            """crear el objeto paciente"""
            cirugia = Vacunas(
                nombrePaciente=cir['nombrePaciente'],
                FechaAtencion = cir['FechaAtencion'],
                motivo=cir['motivo'],
                diagnostico=cir['diagnostico'],
                tratamiento=cir['tratamiento'], 
                observacion=cir['observacion'],
                valor= cir['valor']
            )
            print("datos validos")
            cirugia.save()
            """Limpiar el formulario"""
            form = ''
            return redirect('/cirugia')

    data={'form': form, 'titulo': 'Crear cirugia'}
    return render(request,'crearcirugia.html', data)

def eliminarcirugia(request,id):
    cirugia = Cirugias.objects.get(id=id)
    cirugia.delete()
    return redirect('/cirugia')    

def editarcirugia(request,id):
    cirugia = Cirugias.objects.get(id=id)
    form = Cirugias(instance=cirugia)
    if (request.method =='POST'):
        form = Cirugias(request.POST, instance=cirugia)
        if (form.is_valid()):
            form.save()
            return redirect('/cirugia')
    data={'form': form, 'titulo': 'Editar cirugia'}
    return render(request,'crearcirugia.html', data)
 