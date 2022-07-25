from django import forms
from .models import Empleado

class EmpleadoForms(forms.ModelForm):
    nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={"placeholder":"Nombre"}))
    apellido = forms.CharField(label="Apellido", required=True, widget=forms.TextInput(attrs={"placeholder":"Apellido"}))
    correo = forms.EmailField(label="Correo", required=True, widget=forms.TextInput(attrs={"placeholder":"Correo"}))
    telefono = forms.IntegerField(label="Telefono", required=True, widget=forms.TextInput(attrs={"placeholder":"Telefono"}))
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'correo', 'telefono']

class EmpleadoUpdateForms(forms.ModelForm):
    nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={"placeholder":"Nombre", "value":"{{empleado.nombre}}"}))
    apellido = forms.CharField(label="Apellido", required=True, widget=forms.TextInput(attrs={"placeholder":"Apellido", "value":"{{empleado.apellido}}"}))
    correo = forms.EmailField(label="Correo", required=True, widget=forms.TextInput(attrs={"placeholder":"Correo", "value":"{{empleado.correo}}"}))
    telefono = forms.IntegerField(label="Telefono", required=True, widget=forms.TextInput(attrs={"placeholder":"Telefono", "value":"{{empleado.telefono}}"}))
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'correo', 'telefono']
