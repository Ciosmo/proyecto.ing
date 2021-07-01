from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import DatosAbogado


class AbogadoForm(ModelForm):
    class Meta:
        model = DatosAbogado
        fields = ['rut', 'nombre_abogado','universidad', 'annios_experiencia', 'abogado']
        widgets = {
            'rut' : forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nombre_abogado' : forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'universidad' : forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'annios_experiencia' : forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
