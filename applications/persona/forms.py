from  django import forms
from django.forms import widgets

from .models import Empleado

# si colocas 'mf' puedes utilizar el djanator para generar la clase

class EmpleadoForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:
        """Meta definition for Empleadoform."""

        model = Empleado
        fields = ('first_name', 'last_name', 'job', 'habilidad', 'departamento')

        widgets = {
            'habilidad': forms.CheckboxSelectMultiple()
        }
