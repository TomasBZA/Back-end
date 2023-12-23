from django import forms
from .models import Inscrito, Institucion

class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = ['nombre']

class InscritoForm(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = ['nombre', 'telefono', 'institucion', 'estado', 'observacion']