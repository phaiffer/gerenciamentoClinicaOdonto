from django import forms
from ..models import Dependente


class DependenteForm(forms.ModelForm):
    class Meta:
        model = Dependente
        fields = ['nome', 'nascimento', 'tipo']
        exclude = ['paciente', ]
