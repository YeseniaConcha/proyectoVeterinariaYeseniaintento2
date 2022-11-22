from django.shortcuts import render,redirect
from vaterinariaAPP.models import Veterinaria, Dueno, Mascota, Estetica, Vacunas, Cirugias
from django.db.models import Avg, Max, Min, Sum,Count
from vaterinariaAPP.forms import *



# Create your views here.
def index(request):
    return render (request, 'index.html')


# consulta
def VeterinariaDataView(request):
    listapacientes = Veterinaria.objects.all()
    

    promedio =Veterinaria.objects.all().aggregate(Avg('valor'))
    suma = Veterinaria.objects.all().aggregate(Sum('valor'))
    total = Veterinaria.objects.all().aggregate(Count('valor'))
    maximo = Veterinaria.objects.all().aggregate(Max('valor'))
    minimo = Veterinaria.objects.all().aggregate(Min('valor'))


    data = {
        'veterina': listapacientes,
        'promedio': promedio,
        'total': total,
        'suma': suma,
        'maximo': maximo,
        'minimo': minimo
        }
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

"""dueño"""
def DuenoDataView(request):
    listadueño = Dueno.objects.all()
    data = {'due': listadueño}
    return render(request, 'dueño.html', data)

def crearDueno(request):
    form = DuenoForm()
    if (request.method =='POST'):
        form = DuenoForm(request.POST)
        if (form.is_valid()):
            
            """Rescatar los datos del formulario"""
            due = form.cleaned_data
            """crear el objeto paciente"""
            dueño = Dueno(
                nombreDueño=due['nombreDueño'],
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
    form = DuenoForm(instance=dueño)
    if (request.method =='POST'):
        form = DuenoForm(request.POST, instance=dueño)
        if (form.is_valid()):
            form.save()
            return redirect('/dueño')
    data={'form': form, 'titulo': 'Editar dueño'}
    return render(request,'creardueño.html', data)

"""mascota"""
def MascotaDataView (request):
    listamascota = Mascota.objects.all()
    data = {'mas': listamascota,}
    return render(request, 'mascota.html', data)

def crearMascota(request):
    form = MascotaForm()
    if (request.method =='POST'):
        form = MascotaForm(request.POST)
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
            return redirect('/mascotas')

    data={'form': form, 'titulo': 'Crear Mascota'}
    return render(request,'crearmascota.html', data)

def eliminarMascota(request, id):
    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    return redirect('/mascotas') 

def editarMascota(request, id):
    mascota = Mascota.objects.get(id=id)
    form = MascotaForm(instance=mascota)
    if (request.method =='POST'):
        form = MascotaForm(request.POST, instance=mascota)
        if (form.is_valid()):
            form.save()
            return redirect('/mascotas')
    data={'form': form, 'titulo': 'Editar mascota'}
    return render(request,'crearmascota.html', data)

"""estetica"""
def EsteticaDataView(request):
    listaestetica = Estetica.objects.all()

    promedio =Estetica.objects.all().aggregate(Avg('valor'))
    suma = Estetica.objects.all().aggregate(Sum('valor'))
    total = Estetica.objects.all().aggregate(Count('valor'))
    maximo = Estetica.objects.all().aggregate(Max('valor'))
    minimo = Estetica.objects.all().aggregate(Min('valor'))

    data = {
        'est': listaestetica,
        'promedio': promedio,
        'total': total,
        'suma': suma,
        'maximo': maximo,
        'minimo': minimo
        }
    return render(request, 'estetica.html', data)
  
def crearEstetica(request):
    form = EsteticaForm()
    if (request.method =='POST'):
        form = EsteticaForm(request.POST)
        if (form.is_valid()):
            
            """Rescatar los datos del formulario"""
            est = form.cleaned_data
            estetica = Estetica(
                nombrePaciente=est['nombrePaciente'],
                FechaAtencion = est['FechaAtencion'],
                motivo=est['motivo'],
                diagnostico=est['diagnostico'],
                tratamiento=est['tratamiento'], 
                observaciones=est['observaciones'],
                valor= est['valor']
            )
            print("datos validos")
            estetica.save()
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

"""vacunas"""
def VacunaDataView(request):
    listaVacunas = Vacunas.objects.all()
    
    promedio =Vacunas.objects.all().aggregate(Avg('valor'))
    suma = Vacunas.objects.all().aggregate(Sum('valor'))
    total = Vacunas.objects.all().aggregate(Count('valor'))
    maximo = Vacunas.objects.all().aggregate(Max('valor'))
    minimo = Vacunas.objects.all().aggregate(Min('valor'))

    data = {
        'vac': listaVacunas,
        'promedio': promedio,
        'total': total,
        'suma': suma,
        'maximo': maximo,
        'minimo': minimo
        }

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
                observaciones=vac['observaciones'],
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
    form = VacunaForm(instance=vacuna)
    if (request.method =='POST'):
        form = VacunaForm(request.POST, instance=vacuna)
        if (form.is_valid()):
            form.save()
            return redirect('/vacuna')
    data={'form': form, 'titulo': 'Editar vacuna'}
    return render(request,'crearvacuna.html', data)

"""cirugia"""
def CirugiaDataView(request):

    listaCirugias = Cirugias.objects.all()
    promedio =Cirugias.objects.all().aggregate(Avg('valor'))
    suma = Cirugias.objects.all().aggregate(Sum('valor'))
    total = Cirugias.objects.all().aggregate(Count('valor'))
    maximo = Cirugias.objects.all().aggregate(Max('valor'))
    minimo = Cirugias.objects.all().aggregate(Min('valor'))

    data = {
        'cir': listaCirugias,
        'promedio': promedio,
        'total': total,
        'suma': suma,
        'maximo': maximo,
        'minimo': minimo
    }
    return render(request, 'cirugia.html', data)

def crearcirugia(request):

    form = CirugiaForm()
    if (request.method =='POST'):
        form = CirugiaForm(request.POST)
        if (form.is_valid()):
            
            """Rescatar los datos del formulario"""
            cir = form.cleaned_data
            """crear el objeto paciente"""
            cirugia = Cirugias(
                nombrePaciente=cir['nombrePaciente'],
                FechaAtencion = cir['FechaAtencion'],
                motivo=cir['motivo'],
                diagnostico=cir['diagnostico'],
                tratamiento=cir['tratamiento'], 
                observaciones=cir['observaciones'],
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
    form = CirugiaForm(instance=cirugia)
    if (request.method =='POST'):
        form = CirugiaForm(request.POST, instance=cirugia)
        if (form.is_valid()):
            form.save()
            return redirect('/cirugia')
    data={'form': form, 'titulo': 'Editar cirugia'}
    return render(request,'crearcirugia.html', data)
 