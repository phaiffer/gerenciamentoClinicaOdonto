from django import forms
from django.forms import TextInput, DateInput

from ..models import Paciente


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'email', 'data_nascimento', 'cpf']
        widgets = {
            'data_nascimento': DateInput(
                attrs={'type': "date"}
            )
        }