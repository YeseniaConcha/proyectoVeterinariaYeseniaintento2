"""proyectoVeterinariaYesenia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vaterinariaAPP import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('veterinaria/', views.VeterinariaDataView),
    path('agregar/', views.crearPaciente),
    path('eliminarPaciente/<int:id>', views.eliminarPaciente),
    path('editarPaciente/<int:id>', views.editarPaciente),

    path('dueño/', views.DuenoDataView),
    path('agregarDueño/', views.crearDueno),
    path('eliminarDueño/<int:id>', views.eliminarDueno),
    path('editarDueño/<int:id>', views.editarDueno), 

    path('mascotas/', views.MascotaDataView),
    path('editarMascota/<int:id>', views.editarMascota),
    path('eliminarMascota/<int:id>', views.eliminarMascota),
    path('agregarMascota/', views.crearMascota),

    path('cirugia/', views.CirugiaDataView),
    path('editarCirugia/<int:id>', views.editarcirugia),
    path('eliminarCirugia/<int:id>', views.eliminarcirugia),
    path('agregarCirugia/', views.crearcirugia),

    path('estetica/', views.EsteticaDataView),
    path('editarEstetica/<int:id>', views.editarestetica),
    path('eliminarEstetica/<int:id>', views.eliminarestetica),
    path('agregarEstetica/', views.crearEstetica),

    path('vacuna/', views.VacunaDataView),
    path('editarCirugia/<int:id>', views.editarvacuna),
    path('eliminarCirugia/<int:id>', views.eliminarvacuna),
    path('agregarVacuna/', views.crearvacuna),


]
