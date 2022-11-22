from django import forms
from django.forms import ModelForm
from .models import Veterinaria, Dueno, Mascota, Estetica, Vacunas, Cirugias

class VeterinariaForm(forms.Form):

    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    FechaAtencion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    motivo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    diagnostico = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tratamiento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    observacion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    
    def clean_nombre(self):
        nombre = self.cleaned_data.get['nombre']
        if len(nombre) < 4:
            raise forms.ValidationError("El nombre debe tener al menos 4 caracteres")
        return nombre

    def clean_dueño(self):
        motivo = self.cleaned_data.get['motivo']
        if len(motivo) < 4:
            raise forms.ValidationError("El motivo debe tener al menos 4 caracteres")
        return motivo

    def clean_edad(self):
        diagnostico = self.cleaned_data.get['diagnostico']
        if len(diagnostico) < 4:
            raise forms.ValidationError(" El diagnostico debe ser mayor a 4")
        return diagnostico

    def cleaned_descripcion(self):
        tratamiento = self.cleaned.get['tratamiento']
        if len(tratamiento) < 4:
            raise forms.ValidationError(" El tratamiento debe tener al menos 4 caracteres")
        return tratamiento

    def cleaned_descripcion(self):
        observacion = self.cleaned.get['observacion']
        if len(observacion) < 4:
            raise forms.ValidationError(" La observacion debe tener al menos 4 caracteres")
        return observacion


class VeterinariaForm(ModelForm):
    class Meta:
        model = Veterinaria
        fields ='__all__'
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    FechaAtencion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    motivo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    diagnostico = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tratamiento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    observacion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    
    # def clean_nombre(self):
    #     nombre = self.cleaned_data.get['nombre']
    #     if len(nombre) < 4:
    #         raise forms.ValidationError("El nombre debe tener al menos 4 caracteres")
    #     return nombre

    # def clean_dueño(self):
    #     motivo = self.cleaned_data.get['motivo']
    #     if len(motivo) < 4:
    #         raise forms.ValidationError("El motivo debe tener al menos 4 caracteres")
    #     return motivo

    # def clean_edad(self):
    #     diagnostico = self.cleaned_data.get['diagnostico']
    #     if len(diagnostico) < 4:
    #         raise forms.ValidationError(" El diagnostico debe ser mayor a 4")
    #     return diagnostico

    # def cleaned_descripcion(self):
    #     tratamiento = self.cleaned.get['tratamiento']
    #     if len(tratamiento) < 4:
    #         raise forms.ValidationError(" El tratamiento debe tener al menos 4 caracteres")
    #     return tratamiento

    # def cleaned_descripcion(self):
    #     observacion = self.cleaned.get['observacion']
    #     if len(observacion) < 4:
    #         raise forms.ValidationError(" La observacion debe tener al menos 4 caracteres")
    #     return observacion

class DuenoForm(forms.Form):

    nombreDueño = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    edad = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    
    # def clean_nombre(self):
    #     nombre = self.cleaned_data.get['nombre']
    #     if len(nombre) < 4:
    #         raise forms.ValidationError("El nombre debe tener al menos 4 caracteres")
    #     return nombre

class DuenoForm(ModelForm):
    class Meta:
        model = Dueno
        fields = '__all__'
        
    nombreDueño = forms.CharField(max_length=50)
    edad = forms.IntegerField()    

class MascotaForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    dueño = forms.ModelChoiceField(queryset=Dueno.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    edad = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class MascotaForm(ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'

    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    dueño = forms.ModelChoiceField(queryset=Dueno.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    edad = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class EsteticaForm(forms.Form):

    nombrePaciente = forms.ModelChoiceField(queryset=Mascota.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    FechaAtencion = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    motivo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    diagnostico = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tratamiento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    observaciones = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'})) 

class EsteticaForm(ModelForm):
    class Meta:
        model = Estetica
        fields = '__all__'

    nombrePaciente = forms.ModelChoiceField(queryset=Mascota.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    FechaAtencion = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    motivo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    diagnostico = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tratamiento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    observaciones = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'})) 

class VacunaForm(forms.Form):

    nombrePaciente = forms.ModelChoiceField(queryset=Mascota.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    FechaAtencion = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    motivo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    diagnostico = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tratamiento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    observaciones = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'})) 

class VacunaForm(ModelForm):
    class Meta:
        model = Vacunas
        fields = '__all__'

    nombrePaciente = forms.ModelChoiceField(queryset=Mascota.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    FechaAtencion = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    motivo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    diagnostico = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tratamiento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    observaciones = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'})) 

class CirugiaForm(forms.Form):

    nombre = forms.ModelChoiceField(queryset=Mascota.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    FechaAtencion = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    motivo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    diagnostico = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tratamiento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    observaciones = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'})) 

class CirugiaForm(ModelForm):
    class Meta:
        model = Cirugias
        fields = '__all__'

    nombre = forms.ModelChoiceField(queryset=Mascota.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    FechaAtencion = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    motivo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    diagnostico = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tratamiento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    observaciones = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'})) 
