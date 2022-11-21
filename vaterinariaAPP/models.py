from django.db import models

# Create your models here.
class Dueno(models.Model):

    nombreDueño = models.CharField(max_length=50)
    edad = models.IntegerField()
    class Meta:
        verbose_name = "Nombre dueño"
        verbose_name_plural = "Nombre dueños"

    def __str__(self):
        return self.nombreDueño

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    dueño = models.ForeignKey(Dueno, on_delete=models.CASCADE)
    edad = models.IntegerField()
    descripcion= models.CharField(max_length=100)

    class Meta:
        verbose_name = "Nombre mascota"
        verbose_name_plural = "Nombre mascotas"

    def __str__(self):
        return self.nombre
        
class Veterinaria(models.Model):
    nombrePaciente= models.ForeignKey(Mascota, on_delete=models.CASCADE)
    FechaAtencion = models.CharField(max_length=100)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    observacion = models.CharField(max_length=100)
    valor = models.IntegerField()

    def __str__(self) -> str:
        return self.nombrePaciente

class Estetica(models.Model):
    nombrePaciente= models.ForeignKey(Mascota, on_delete=models.CASCADE)
    FechaAtencion = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    valor = models.IntegerField() 

    class Meta:
        verbose_name = "nombre paciente"
        verbose_name_plural = "nombre pacientes"

    def __str__(self):
        return self.nombrePaciente

class Vacunas(models.Model):
    nombrePaciente = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    FechaAtencion = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    valor = models.IntegerField() 

    class Meta:
        verbose_name = "nombre paciente"
        verbose_name_plural = "nombre pacientes"

    def __str__(self):
        return self.nombrePaciente

class Cirugias(models.Model):
    nombrePaciente = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    FechaAtencion = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    valor = models.IntegerField() 

    class Meta:
        verbose_name = "nombre paciente"
        verbose_name_plural = "nombre pacientes"

    def __str__(self):
        return self.nombrePaciente

